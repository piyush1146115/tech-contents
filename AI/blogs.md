# AI Blogs

-[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [https://www.pinecone.io/learn/vector-database/](https://www.pinecone.io/learn/vector-database/)
- [The last six months in LLMs in five minutes](https://simonwillison.net/2026/May/19/5-minute-llms/)
- [Context engineering with Dex Horthy](https://newsletter.pragmaticengineer.com/p/context-engineering-with-dex-horthy)
- [Pi’s Minimalism Is Its Advantage](https://earendil.com/posts/pi-autoresearch-and-databricks/)
- [The AI Agents Stack (2026 Edition)](https://www.oreilly.com/radar/the-ai-agents-stack-2026-edition/)
    -  We defined an agent as the think-act-observe cycle: The model reasons about a task, takes an action (calls a tool, writes to memory), observes the result, and loops until the task is done. That loop is the atomic unit. Everything in this issue is infrastructure that makes that loop work reliably, at scale, in production.
    - **Layer 1: Models and inference**: How you run the model that powers your agent: call an API, use a managed open weight provider, or self-host.
    - **Layer 2: Protocols and tools**: How your agent calls external tools and APIs: through MCP servers, browser automation, or agent-to-agent protocols.
    - **Layer 3: Memory and knowledge**: How your agent stores and retrieves what it knows: in-context state, vector search, or persistent memory across sessions. “Context engineering” replaced “prompt engineering” as the core discipline. Instead of writing a better prompt, you architect what information the agent sees on every call. The honest take: Most teams overcomplicate memory. Start with conversation history in Postgres and a structured system prompt. Add vector search when your history exceeds context limits. Add agentic memory management only when your agent needs to learn across sessions. The prototype-to-production gap is large. Demo memory works because context windows are big enough. Production memory breaks when conversations get long and your agent starts forgetting the important parts.
    - **Layer 4: Frameworks and SDKs**: Every major AI lab now ships its own agent SDK. OpenAI has the Agents SDK (evolved from Swarm). Google released ADK. Microsoft has Semantic Kernel and AutoGen. Hugging Face built smolagents. Two years ago, LangChain was the only game. Now you pick between three camps: provider SDKs that are fast to start but locked to one model, graph-based frameworks like LangGraph that are portable but require more setup, or no framework at all. That choice didn’t exist in 2024. Provider SDKs manage state for you. LangGraph makes you define every state transition explicitly. Build-it-yourself means you roll your own. Lock-in risk is the highest in the stack. Your orchestration code doesn’t port. A LangGraph agent rewritten for CrewAI is a new codebase. Provider SDKs are worse because you’re locked to one model too. The prototype-to-production gap is large. Demo works because nothing goes wrong. Production means handling tool failures, retries, timeouts, and humans who need to approve before the agent acts.
    - **Layer 5: Eval and observability** : How you measure whether your agent is doing its job: tracing runs, scoring outputs, and catching regressions before users do. State management matters here because your agent runs 12 steps, step 3 picked the wrong tool, and steps 4–12 were doomed from there. If your eval only checks the final output, you’ll never know why. Lock-in risk is moderate. Most tools export OpenTelemetry traces, so switching observability providers is doable, but switching eval frameworks means rebuilding your test suites. The prototype-to-production gap is the biggest of any layer. Most prototypes have zero eval. You don’t feel the pain until production users find the failures for you.
    - **Layer 6: Guardrails and safety**: How you stop your agent from doing things it shouldn’t: filtering inputs, authorizing tool calls, and validating outputs. Guardrails now means authorizing tool calls, enforcing rate limits, and validating what the agent actually did. Guardrails need to know what the agent is doing right now to decide what it shouldn’t do next. That means tracking agent state in real time. Lock-in risk is low because most guardrails are custom policy code you write yourself. NeMo Guardrails is the closest thing to a framework, but you’ll still write most rules from scratch. The prototype-to-production gap is effectively infinite. Your demo has no guardrails because nobody’s trying to break it. Production will.
- [Building Production-Ready AI Agents in 2026](https://mlflow.org/articles/building-production-ready-ai-agents-in-2026/)
    - The set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts
    - Context Engineering vs. Prompt Engineering
    - You still need to know how to write system instructions that don't contradict themselves. But once your agent has tools, memory, and a retrieval layer, the act of writing a good prompt is a tiny fraction of the work.
    - Prompt engineering is essential for one-off tasks, but context engineering is what matters for complex tasks and agent systems that maintain conversation history and pull in external data across many turns.
    - The context engineering system comes down to four questions:
        - What do we fetch?
        - When do we fetch it?
        - How do we compress it?
        - When do we throw it away?
    - The four pillars of Context engineering
        - Instructions / System Prompt
        - Retrieval
        - Memory
        - Tools
    - Context Engineering for AI Coding Agents
    - Common Failure Modes (and How to Avoid Them)
        - Context Overload, Context Distraction, and Context Confusion
        - Stale or Irrelevant Retrieval
        - Lost in the Middle: The headline finding is that model performance "is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models."
    - Tools and Frameworks for Context Engineering
        - Vector Databases
        - Orchestration
        - Code Intelligence
    
- [Agent observability powers agent evaluation](https://www.langchain.com/blog/agent-observability-powers-agent-evaluation)
    - You can't build reliable agents without understanding how they reason, and you can't validate improvements without systematic evaluation. This article explains the primitives for agent observability, how to evaluate agents at different granularities, and how production traces become the foundation for continuous improvement.
    - You don't know what your agents will do until you actually run them — which means agent observability is different and more important than software observability
    - Agents often do complex, open-ended tasks, which means evaluating them is different than evaluating software
    - Because traces document where agent behavior emerges, they power evaluation in a multitude of ways
    - Agent evaluation ≠ software evaluation
    - Agent observability ≠ software observability
    -  Traditional software testing relies on deterministic assertions: write tests that check output == expected_output, verify they pass, then ship. Online evaluation (A/B tests, product analytics) measures business impact separately. Evaluating agents differ from evaluating software in a few key ways:
        - You're testing reasoning, not code paths
        - Production becomes your primary teacher
            - With agents, production plays a different role. Because every natural language input is unique, you can't anticipate how users will phrase requests or what edge cases exist. Production traces reveal failure modes you couldn't have predicted and help you understand what "correct behavior" actually looks like for real user interactions. This shifts how you think about evaluation: production isn't just where you catch missed bugs. It's where you discover what to test for offline. Production traces become test cases, and your evaluation suite grows continuously from real-world examples, not just engineered scenarios.
    - The primitives of agent observability:
        - Runs: A single execution step (one LLM call with its input/output)
        - Traces: A complete agent execution showing all runs and their relationships
        - Threads: Multi-turn conversations grouping multiple traces over time
    - Runs: capturing what the LLM did at a single step
    - Traces: capturing trajectories
    - Threads: multi-turn conversation context
    - Agent traces are massive. While a typical distributed trace might be a few hundred bytes, agent traces can be orders of magnitude larger. For complex, long-running agents, traces can reach hundreds of megabytes. This context is necessary for debugging and evaluating the agent's reasoning.
    - 
















