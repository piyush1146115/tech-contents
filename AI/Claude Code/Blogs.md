# Blogs related to claude code

- [Reduce Claude Code Costs 60% With These Four Habits](https://systemprompt.io/guides/claude-code-cost-optimisation)
    - Set MAX_THINKING_TOKENS to 10,000. Thinking tokens are the single biggest cost driver. This change alone reduces spend by 30-40%.
    - Default to Sonnet, not Opus. Sonnet handles 80% of daily tasks at one fifth the cost. Switch to Opus only for complex reasoning.
    - Clear context between tasks. Every task inherits all previous context. Start fresh with /clear to avoid paying for stale tokens.
    - Be specific in prompts. Vague prompts lead to back-and-forth exchanges. Save 50,000+ tokens per task with specific, file-named requests.
    - Claude Code charges based on tokens, which are roughly four characters each. A task that generates 5,000 output tokens costs $0.375 with Opus and $0.02 with Haiku. Over hundreds of tasks per month, these differences compound significantly.
    - Track Spend in Real Time With the `/cost` Command. The most impactful cost optimisation is choosing the right model for each task. Most developers default to the most powerful model available and never switch. A good habit is starting every session on Sonnet and only switching to Opus when hitting a task that Sonnet struggles with. This single habit can reduce costs by roughly 40%.
    - The `/compact` command is one of Claude Code's most useful cost management features. It summarises the current conversation into a condensed form, reducing the context size that is sent with subsequent prompts.
    - Optimise CLAUDE.md for Token Efficiency
    - The most effective teams keep CLAUDE.md under 50 lines and use it as an index, not a knowledge dump. Each line points to a detailed file that Claude loads only when relevant. Some teams run under 30 lines. Deep context loads on demand instead of riding along with every prompt.  Review your CLAUDE.md monthly. Delete anything that refers to completed features, resolved issues, or outdated conventions. It is not uncommon to find instructions about a database migration that was completed six months earlier, still being sent with every prompt.
    - Grouping related changes into a single prompt is more efficient than making them one at a time. Each separate prompt carries the full context overhead. Five separate prompts about five related changes cost roughly five times more than a single prompt that addresses all five.
    - Daily habits
        - Start the day on Sonnet, not Opus. Switch up only when a task truly needs it.
        - Run `/cost` at the start and end of every session so you have a baseline.
        - Use `/clear` between unrelated tasks. The rule is one conversation per intent.
        - Write specific prompts that name files and state the desired outcome in a single sentence.
        - Set `MAX_THINKING_TOKENS=10000` in your environment once and forget about it.
    - Weekly habits
        - Review session costs for the week. Flag any task that cost more than twice its peer average.
        - Trim `CLAUDE.md`. Delete stale instructions, move long procedures into skill files
        - Audit which MCP servers are actually used. Remove the ones that are not.
        - Compare Sonnet and Opus usage ratios. Opus should be a minority of sessions.
    - Monthly habits
        - Export usage data from the Anthropic Console and compute cost per task for the month.
        - Reassess which models different task types are landing on.
        - Check whether new Claude API pricing has shifted the cost-benefit of any workflow.
        - Share the scorecard with the team so cost literacy spreads.
- [Manage costs effectively](https://code.claude.com/docs/en/costs)
    - Add custom compaction instructions: `/compact Focus on code samples and API usage` tells Claude what to preserve during summarization.
    - Track your costs using the `/usage` command
    - Choose a right model
    - Reduce MCP server overhead
    - Install code inteligence plugins: https://code.claude.com/docs/en/discover-plugins#code-intelligence
    - Offload processing to hooks and skills
    - For example, this PreToolUse hook filters test output to show only failures: https://code.claude.com/docs/en/costs#offload-processing-to-hooks-and-skills
    - Move instructions from CLAUDE.md to skills
    - Adjust extended thinking
    - Delegate verbose operations to subagents
    - Write specific prompts: Vague requests like “improve this codebase” trigger broad scanning. Specific requests like “add input validation to the login function in auth.ts” let Claude work efficiently with minimal file reads.
    - Work efficiently on complex tasks
        - If Claude starts heading the wrong direction, press Escape to stop immediately. Use /rewind or double-tap Escape to restore conversation and code to a previous checkpoint.
        - Give verification targets: Include test cases, paste screenshots, or define expected output in your prompt. When Claude can verify its own work, it catches issues before you need to request fixes.
        - Test incrementally: Write one file, test it, then continue. This catches issues early when they’re cheap to fix.

- [From Tokenmaxxing to Token Discipline: The 2026 Reckoning in AI-Assisted Engineering](https://corti.com/from-tokenmaxxing-to-token-discipline-the-2026-reckoning-in-ai-assisted-engineering/)
    - "Tokenmaxxing" is the practice of treating AI token consumption as a proxy for productivity — the more tokens your agents burn, the more "productive" you are assumed to be.
    -  Per-developer token consumption rose roughly 18.6× in nine months — a volume increase that swamps any per-token price decline.
    - The correct unit is cost per accepted task — a merged pull request, a resolved ticket — not cost per token. Token volume is a useful diagnostic only once it's tied to acceptance criteria.
    - More tokens can actively degrade quality. Jellyfish found heavy token users were about 2× more productive but spent 10× the tokens (Business Model Analyst) — a sharply diminishing return.
    - Gartner separately projects inference cost on a trillion-parameter model falling more than 90% by 2030, while noting agentic workflows consume 5–30× more tokens per task than a standard chatbot — so the per-token deflation and the per-task inflation are racing each other.
    - This is the part that matters most for engineers, because the answer to "tokenmaxxing is expensive" is not "use AI less." It's "engineer what goes into the context window." The discipline now has a name — context engineering — and a fairly settled toolkit.
    -  Context engineering becomes a first-class engineering skill. The differentiator stops being access to a frontier model — everyone has that — and becomes the harness around it: compaction strategy, sub-agent decomposition, retrieval design, note-taking discipline, and routing logic.
- [Claude Code Token Optimization Guide](https://buildtolaunch.substack.com/p/claude-code-token-optimization)
    - Install context-mode to Cut MCP Token Output 50–90%: https://github.com/mksglu/context-mode
    - Use RTK to Compress Bash Output Before It Enters Context: https://github.com/rtk-ai/rtk: installs a PreToolUse hook that rewrites Bash commands to compressed equivalents before the output reaches Claude. A git status or cargo test that would dump thousands of tokens gets filtered down to the signal. Saves 60–90% on common dev commands.
    - Keep CLAUDE.md Under 500 Tokens to Lower Your Constant Baseline
```
# CLAUDE.md

## Rules
- Use TypeScript strict mode
- Write tests for every new function
- Follow existing patterns in the codebase

## Key Files
- API routes: see src/api/README.md
- Database schema: see docs/schema.md
- Style guide: see docs/style-guide.md
```

- [How Claude Code works in large codebases: Best practices and where to start](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start)
    - Claude Code navigates a codebase the way a software engineer would: it traverses the file system, reads files, uses grep to find exactly what it needs, and follows references across the codebase. It operates locally on the developer’s machine and doesn’t require a codebase index to be built, maintained, or uploaded to a server. 
    - This means the quality of Claude's navigation is shaped by how well the codebase is set up, layering context with CLAUDE.md files and skills. If you ask it to find all instances of a vague pattern across a billion-line codebase, you’ll hit context-window limits before the work begins
    - The harness matters as much as the model
    - The harness is built from five extension points—CLAUDE.md files, hooks, skills, plugins, and MCP servers—each serving a different function.
    - Hooks make the setup self-improving. Most teams think of hooks as scripts that prevent Claude from doing something wrong, but their more valuable use is continuous improvement. A stop hook can reflect on what happened during a session and propose CLAUDE.md updates while the context is fresh.
    - Skills keep the right expertise available on-demand without bloating every session. In a large codebase with dozens of task types, not all expertise needs to be present in every session. Skills solve this through progressive disclosure, offloading specialized workflows and domain knowledge that would otherwise compete for context space and loading them only when the task calls for it.
    - Skills can also be scoped to specific paths so they only activate in the relevant part of the codebase. A team that owns a payments service can bind their deployment skill to that directory, so it never auto-loads when someone is working elsewhere in the monorepo.
    - Plugins distribute what works. One challenge with large codebases is that good setups can stay tribal. A plugin bundles skills, hooks, and MCP configurations into a single installable package, so when a new engineer installs that plugin on day one, they will immediately have the same context and capabilities as those who have been using Claude already. Plugin updates can be distributed across the organization through managed marketplaces. 
    - Language server protocol (LSP) integrations give Claude the same navigation a developer has in their IDE. Most large-codebase IDEs already have an LSP running, powering "go to definition" and "find all references." Surfacing this to Claude gives it symbol-level precision: it can follow a function call to its definition, trace references across files, and distinguish between identically named functions in different languages.
    - Subagents split exploration from editing. A subagent is an isolated Claude instance with its own context window that takes a task, does the work, and returns only the final result to the parent. 
    - Making the codebase navigable at scale
        - Keeping CLAUDE.md files lean and layered. Claude loads them additively as it moves through the codebase: root file for the big picture, subdirectory files for local conventions. The root file should be pointers and critical gotchas only; everything else drifts into noise.
        - Initializing in subdirectories, not at the repo root. Claude works best when it's scoped to the part of the codebase that's actually relevant to the task. In monorepos, this can feel counterintuitive because tooling often assumes root access, but Claude automatically walks up the directory tree and loads every CLAUDE.md file it finds along the way, so root-level context is never lost.
        - Building codebase maps when the directory structure doesn’t do the work: For codebases with hundreds of top-level folders, this works best as a layered approach: the root file describes only the highest-level structure, and subdirectory CLAUDE.md files provide the next level of detail, loading on demand as Claude moves through the tree. For simpler cases, @-mentioning the specific files or directories Claude should reference can do the same job.
        - Running LSP servers so Claude searches by symbol, not by string: Grep for a common function name in a large codebase returns thousands of matches and Claude burns context opening files to figure out which matters. LSP returns only the references that point to the same symbol, so the filtering happens before Claude reads anything. Setting this up requires installing a code intelligence plugin for your language and the corresponding language server binary; the Claude Code documentation covers the available plugins and troubleshooting.
    - Actively maintaining CLAUDE.md files as model intelligence evolves
        - Teams should expect to do a meaningful configuration review every three to six months, but it's also worth doing one whenever performance feels like it's plateaued after major model releases. 
    - Assigning ownership for Claude Code management and adoption
        - An emerging role in several organizations is an agent manager: a hybrid PM/engineer function dedicated to managing the Claude Code ecosystem. 
        

- [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
    - When you send a message to Claude, the prompt is only a small part of the context it gets. Much of your context is assembled from your system prompt, Skills, CLAUDE.md files, memory, and other sources. We call this context engineering, and it makes a big impact on the results you generate when using Claude Code or in building your own agents.
    - Now: Let Claude use judgement
    - Then: Give Claude examples, Now: Design interfaces
    - Then: Put it all upfront, Now: Use progressive disclosure
        - The same can be applied to your own CLAUDE.md and Skill.md files. A common myth is that you want to make these a central repository for every known practice that you might run into, because Claude would not find it otherwise. Instead, consider having a tree of files that can be loaded at the right time.
    - Then: Repeat yourself, Now: Simple tool descriptions
    - Then: Memory in CLAUDE.md files, Now: Auto-memory
        - Instead, Claude now automatically saves memories that are relevant to the work and to you. 
    - Then: Simple specs, Now: Rich references
    - System Prompt:
        - A system prompt is heavily tied to the product context. It tells Claude what product it’s operating in and what it’s doing. For Claude Code, you will likely never modify this, but if you are building your own agent harness, this is where you should spend a lot of time.
    - CLAUDE.md:
        - Keep your CLAUDE.md lightweight and briefly describe what your repo is for, but spend most of the tokens on gotchas inside of the codebase. For example, you may organize your code to keep types in one monolithic file and nowhere else. Avoid stating ‘the obvious’ things Claude should know by looking at your file system or your repo. 
        - Use progressive disclosure heavily, for example if you have several unique instructions on how to verify your work, create a verification skill and reference it from your CLAUDE.md.
    - Skills
        - Think of skills as lightweight guides to let Claude find information when needed. Avoid making them overconstrained, except in highly important areas. For long skills, try and use progressive disclosure as much as possible- divide it into many files and split them out. It’s best when skills encode particular opinions, knowledge, or best practices that are particular to you, your team, or product.
    - References
        - You can @ mention files to include them as references. References allow Claude to refer to in-depth information about the current plan. This might be in specs files, mockups, or even entire codebases. Generally you should prefer files that are in code as it provides clear, high-fidelity instructions to Claude in a language it knows very well. For example, a HTML mockup of a design will generally produce better results than a description of the design or a screenshot.
    - Try simplifying
        - Across your system prompt, skills, and CLAUDE.md files, you may need to simplify just like we did. We rolled out a new command called `claude doctor,` which will help you do this automatically as well.

- [Auto mode is default now](https://claude.com/blog/auto-mode-default-in-claude-code)