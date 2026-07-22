# Notes related to hermes agent

## The system at a glance 

Hermes is a Python agent with an unusually wide surface. Group it into five layers:

- Core runtime: The agent turn loop: model calls, tool dispatch, retries, context compression, persistence.
- Tools & skills: Self-registering tools grouped into toolsets; agent-authored skills as reusable procedures.
- Learning loop: The self-improvement flywheel: memory, session search, skill creation/refinement, delegation.
- Integration: The multi-platform gateway + the model-provider abstraction — how it reaches users and models.
- Deployment: Pluggable execution backends, the cron scheduler, and the ACP/MCP protocol edges.

## End-to-end message flow

How an inbound message from any channel becomes a reply. The gateway normalizes; the core runtime reasons; a backend does the work; the gateway delivers.

```
INBOUND
   Telegram / Discord / Slack / WhatsApp / Signal / CLI / HTTP API
        │
        ▼
   BasePlatformAdapter          gateway/platforms/base.py:2317
        │   normalize → MessageEvent, key = (platform, user_id, chat_id, thread_id)
        ▼
   GatewayRunner                gateway/run.py:3029
        │   load/create session (SQLite), pick profile
        ▼
   AIAgent.run_conversation()   agent/conversation_loop.py:588   ◀── THE TURN LOOP
        │
        ├─▶ LLM provider     resolved by ProviderProfile / api_mode   providers/base.py:38
        │
        ├─▶ Tools            handle_function_call() → registry.dispatch()   model_tools.py:1025
        │        │
        │        ▼
        │   Execution backend    local │ docker │ ssh │ modal │ daytona │ singularity
        │                        tools/environments/*  (selected by env_type)
        │
        ▼
   final response
        │
        ▼
   DeliveryRouter → adapter.send()    gateway/delivery.py
        │
        ▼
 OUTBOUND  (back to the originating channel)
 ```

## The bets that make Hermes distinctive

1. Prompt-cache discipline everywhere. The api_content sidecar and frozen memory snapshots exist so a changing agent still presents a byte-stable prefix — cheap multi-turn inference is a first-class design constraint, not an afterthought.
2. One gateway, many channels. A single process + capability-flagged adapters, rather than per-platform bots. Lower ops burden, shared session store.
3. Compute is pluggable. The same agent runs against local/Docker/SSH/Modal/Daytona/Singularity behind one BaseEnvironment — including serverless backends that hibernate when idle.
4. Improvement without training. The learning loop is entirely file- and DB-backed (skills, memory, FTS5) — no fine-tuning, so it works with any model.

**Where a reviewer should push:**
- Monolith risk. run_conversation() (~3,900 lines) and AIAgent (~6,000 lines) concentrate enormous branching behavior — great control, hard to test and reason about in isolation.
- Autonomy vs. safety. Agent-authored skills and memory are powerful but are attack surface; note the optional skills.guard_agent_created scan and memory injection/exfil scans (off/limited by default).
- Surface area. Six backends, ~8 channels, three provider protocols, two agent-facing protocols (ACP/MCP) — enormous capability, but a large maintenance and security footprint to evaluate.

## Anatomy of a single Hermes turn

One user message in, one final response out — and everything the loop does in between. This is the spine every other subsystem hangs off.

A "turn" = one user message and all the model/tool iterations Hermes runs before it returns a final response. Inside a turn there can be many API calls.

The whole loop is essentially one function: run_conversation() in agent/conversation_loop.py:588 — roughly 3,900 lines.

The eight phases of a turn
- Prologue (once per turn): does the heavy setup: restore or rebuild the system prompt, refresh MCP tools, create the SQLite session row, sanitize the user message, hydrate todos/nudges, prefetch memory, and — importantly — persist the user message before any API call so a crash mid-turn loses nothing. Returns a TurnContext.
- Loop gate: iterate while api_call_count < max_iterations and the per-turn IterationBudget has room. A "grace call" grants one final attempt when the budget is spent, so the turn ends with a real answer rather than a hard stop.
- Message assembly: repair/validate message alternation, inject memory + plugin context at API-call time only, replay the api_content sidecars, and add Anthropic cache_control breakpoints on the system prompt and last 3 messages.
- Preflight compression check: estimate request tokens; if over threshold (and not in cooldown, and <3 attempts), compress the context, refund the iteration, and loop.
- API call: build kwargs, run request middleware + pre_api_request hooks, then call the model via _interruptible_streaming_api_call() (90s stale-stream / 60s read-timeout health checks). Response shape is validated per transport (Anthropic / Bedrock / OpenAI / Codex).
- Tool-call validation: check tool names (fuzzy auto-repair, e.g. read_flie → read_file), validate JSON arguments (empty → {}, truncation detection, up to 3 retries), then dedupe and cap calls.
- Tool execution: Each result is formatted, redacted, and appended as a tool message.
- Continue or exit: — if finish_reason == "tool_calls", loop back to phase 3. Otherwise extract the text and fall through to turn_finalizer agent/turn_finalizer.py: flush to SQLite, fire callbacks, trigger background memory/skill nudges, run optional verify-on-stop gates.

### Three details a reviewer should not miss:

1.  The api_content sidecar
Each stored message carries a hidden `api_content` field: the exact bytes sent to the provider last turn. On the next turn those bytes are replayed verbatim, while live memory/context is injected fresh at API time and never written back to the stored message. The point is prompt-cache stability — the cached prefix stays byte-identical, so memory can change between turns without invalidating the cache.
2. In-turn compression protects head and tail summarizes the middle of a long conversation with a cheap auxiliary model, while preserving the protected head (system prompt, first user/assistant/tool exchange) and the last N turns. The summary is injected as a user message prefaced "this is reference-only background." It can also rotate to a child session. Don't confuse this with trajectory_compressor.py — that's offline batch post-processing of finished trajectories for training data, a different thing entirely.
3. Self-healing inputs: Iteration budget with a grace call, fuzzy tool-name repair, JSON-argument recovery, empty-response prefill/retry — the loop assumes the model will misbehave and recovers in-band instead of failing the turn. For a reviewer: this is robustness bought with a lot of special-case code paths.

### State: what persists, what doesn't

Conversation state is just a `List[Dict]` of messages in memory — role, content, tool_calls, plus internal fields like api_content and _compressed_summary. Durably, everything lands in a single SQLite store, hermes_state.py, in WAL mode (concurrent readers, one writer — needed because the gateway serves many platforms at once) with an FTS5 index over message content for cross-session search. Curated memory (MEMORY.md/USER.md) is frozen into the system prompt at session start and only refreshes next session — the same prompt-cache discipline as the sidecar.

### The reviewer's lens

The core loop is a single ~3,900-line function with deep branching for retries, compression, and provider quirks. That buys real robustness and tight control over prompt-cache bytes — but it concentrates enormous behavior in one place with high cyclomatic complexity. When you evaluate Hermes, this is the central tradeoff to have a view on: in-band resilience & cache control vs. testability & modularity.

## The self-improving learning loop

Hermes's headline claim is that it gets better across sessions — without retraining. Most agent frameworks are stateless between sessions, or bolt on a vector DB. Hermes's claim is a closed loop where the agent itself captures experience and reads it back later — and it does this with plain files and one SQLite database, no model fine-tuning at all. Everything the agent "learns" is written to disk and re-read — Markdown memory, Markdown skills, and SQLite session history. Nothing updates the model weights. That's why it works with any model you switch to (recall the provider abstraction), and why the whole loop runs on a $5 VPS. 

```
        ┌──────────────  a turn does work  ──────────────┐
        │                                                 ▼
   RECALL next time                                 CAPTURE experience
   starts smarter                                   (agent-initiated)
        ▲                                                 │
        │            ┌──────────── persisted to ──────────┤
        │            │                                     │
   session_search ◀──┤  SQLite + FTS5      (conversations) │
   read a skill    ◀─┤  ~/.hermes/skills/  (SKILL.md)      │
   frozen memory   ◀─┤  MEMORY.md / USER.md (curated)      │
        │            └─────────────────────────────────────┘
        └───────── periodic "nudges" prompt the agent to persist ───────┘
```

### The six mechanisms

Six independent, agent-driven mechanisms make up the loop.
- Curated memory: Writes durable facts to MEMORY.md and a model of you to USER.md. Nudged periodically to persist what it learned.
- Skill creation: After a hard task, writes a reusable SKILL.md capturing the approach
- Skill refinement: On reuse, patches/rewrites the skill — a background-review fork may only edit what it has read.
- Delegation: Spawns isolated subagents (sync/batch/background) so parallel work never pollutes the parent context.
- Session lineage: Links parent/branch/compression/delegate sessions so history stays navigable and prunable.
- Session search: Recalls past conversations at zero LLM-token cost — the deep dive below.

### Deep dive: session search & FTS5

"Searches its own past conversations" is the concrete claim. The engine is FTS5 — SQLite's built-in full-text search. You build a virtual table that maintains an inverted index over text, then query it with MATCH (not LIKE), getting tokenization, boolean/phrase/prefix queries, BM25 relevance ranking, and highlighted snippet() excerpts — all inside the same .db file. No search server to run: that's what makes it viable on a tiny VPS.

#### Read path — search_messages(), zero LLM cost

```
query
  └▶ sanitize + cap        strip FTS specials, quote hyphen/dot terms, cap length (:5335)
       └▶ CJK router
            ├─ ≥3 CJK chars/token ─▶ messages_fts_trigram MATCH   (:5585)
            ├─ 1–2 CJK chars ──────▶ LIKE substring fallback
            └─ otherwise ──────────▶ messages_fts MATCH           (:5512)
                 └▶ ORDER BY rank   ← BM25 relevance             (:5509)
                      └▶ snippet(…, '>>>','<<<', 40)  excerpts    (:5543)
                           └▶ top-N sessions  →  (optional) Scroll into full text
```

The whole Discovery pass is a pure SQL query — no model call. The agent only spends tokens if the ranked snippets look worth reading and it scrolls into a session. That's why routine self-recall is affordable, and it's load-bearing for the whole loop.

