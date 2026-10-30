# Stanford CME295 Transformers & LLMs | Autumn 2026 | Lecture 1 - Transformers

Link: https://www.youtube.com/watch?v=114i2Kz-LZA&t=272s


## Goals and Audience

- Understand how Transformers work and how they relate to LLMs
- Learn how LLMs are trained and used in various applications

Audience:
- Interested in LLMs
    - Career goal
    - Personal project
    - AI Literacy or curiosity
- Prerequisite: machine learning basics, linear algebra

## Reference Materials

Book: Super Study Guide: Transformers and Large Language Models
- https://superstudy.guide/transformers-large-language-models/
- https://leanpub.com/transformers-large-language-models/
- Cheatsheet: https://github.com/afshinea/stanford-cme-295-transformers-large-language-models

- Machine learning Cheatsheet: https://github.com/afshinea/stanford-cs-229-machine-learning

## Contents

- Introduction
- Tokenization
- Word representation
- Self-attention mechanism
- Transformer architecture
- End-to-end example
- Discussion

## Tokenization

- Model understands numbers, not text. The process of diving the text into indivisible entities is what is called tokenization.
- Token = character
- Three level of tokenization: word level, subword level and character level
- Subword level tokenizer is the most popular now
- **BPE** is a subword tokenizer. That stands for byte pair encoding.

### Special Tokens

- UNK - Unknown ("out of vocabulary")
- BOS - Begining of Sequence
- EOS - End of Sequence
- PAD - Padding

## Word representation

