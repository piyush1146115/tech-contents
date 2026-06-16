# Reflection Design Patterns

## Reflecting to improve outputs of a task

- Write code for task X -> LLM -> Code v1 -> execute code -> LLM (Reflect on code output or errors and write improved second draft) -> Code v2

## Why not just direct generation?

- What is Zero, one and few-shot prompting?
    - Zero-shot (no examples)
    - One-shot (single example)
    - Two-shot (two examples), Few-shot (multiple examples)
- Reflection consistently outperforms direct generation on a variety of tasks
- Tips for writing reflection prompts:
    - Clearly indicate the reflection action
    - Specify criteria to check

## Reflection with a different LLM

- LLM: Code generation -> Write python code to generate visualization that answers the user's question
- LLM2: Reflection -> You are an expert data analyst who provides constructive feedback on visualization
