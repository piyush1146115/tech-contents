# Module 1: Introduction to Agentic Workflows

## What is Agentic AI

An Agentic AI workflow is a process where an LLM-based app executes multiple steps to complete a task.

- Agentic workflow:

## Degree of Autonomy

- Less autonomous:
    - Write an essay about blackholes
- More autonomous:
    - Agent decides on it's own to make decisions to use tools, show output

## Benefits of agentic AI

- Parallelization for speed
- Much better performance
- Modular: can add or update tools, swap out models

## Agentic AI Applications

What tasks is agentic AI suited to?
- Clear, step-by-step process
- Standard procedures to follow
- Text assets only
- Steps not known ahead of time
- Plan/solve as you go
- Multimodal


## Task decomposition

- Example 1: Write an Essay on topic X
- Example 2: 

What building blocks do you have for an agent?
- Models: LLMs - text generation, tool use, information extraction
- Tools: API - Web search, get real-time data
- Information retrieval: Databases, Retrieval Augmented generation
- Code execution: Basic calculator, data analysis

## Evaluating Agentic AI (evals)

- Look for low-quality outputs
    - Extract key information
    - Find relevant customer
    - Write and send response
- Add an evaluation to track the error
- Using LLM as a judge
    - Assign the following essay a quality score between 1 and 5, where 5 is the best: {essay}
- Evaluating Agentic AI
    - Can evaluate using code (objective evals), or LLM-as-judge (subjective evals)
    - Two types of evals: End-to-end and component-level
    - Examine traces to perform error analysis

## Agentic design patterns

1. Reflection: Implementer Agent, Critic Agent
2. Tool use: Web Search Tool, Code Execution Tool
3. Planning
4. Multi-agent collaboration
