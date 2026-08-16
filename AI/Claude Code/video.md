# Videos related to Claude Code

- [1000+ hours of Learning Claude in 15 Minutes (Beginner to Pro)](https://youtu.be/sL5hPovH1vU?si=_1v0tWEPnMgtJeVk)
- [Getting more out of the Claude Platform](https://www.youtube.com/watch?app=desktop&v=7oO37GRhwGk)
    - Prompt caching
    - Different orgs achieved 90% savings with prompt caching
    - Context window engineering: the discipline of deciding what belongs in Claude's context
        - Tool search
            - Keep unused tool schemas out of context
            - tool_search tool
        - Programmatic tool calling
        - Compaction
    - Advisor strategy: Give Sonnet an on-demand intelligence boost at roughly the same cost
    - Better architectural decisions complex tasks, no overhead on simple ones
    


- [Boris Cherny: We Cut 80% of Claude Code’s Prompt](https://youtu.be/qyPCVqFUyDo?si=7e2XSp3wlFwyPWpU)
    - Opus 5
    - System prompt is becoming more leaner, they deleted 80% of system prompt
    - Every 6 months delete your hooks, delete your skills, delete claude.md. See how the model behaves
    - un-hubbling the model for future founders
    - A common mistake of people using is they give Claude way over specific instructions. For modern models, that's actually really not the way to do it. You want to go a little bit higher level. You want to describe the task, you want to describe the guardrails, you want to describe like the exit criteria and then just go with the model cook and come back in a little bit. It does work today
    - The bun rewrite from Zig to Rust was essentially a single dynamic workflow. It took 11 days to rewrite. 
    - Second way to think about it is experiment. Just give yourself freedom to play with the model and do creative things. Often it will surprise you
    - The skill nowadays is less about prompt engineering, and more about figuring out how do you give Claude a hard task that seems a little bit too hard and then how do you make it possible Claude to verify its work along the way
    - Don't listen to the LinkedIn influencers for a magical trick
    - People tend to over-engineer claude code, over-specify things. People are un-learning these
    - Be empirical, forget everything about you learned about past models. Look at the model, try to do a task, see where it struggles.
    - Learn just not the computer science, learn how to apply it as well

