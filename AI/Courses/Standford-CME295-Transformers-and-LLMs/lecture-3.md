# Lecture 3 - LLM Training

## Contents

- Pretraining
- Supervised finetuning
- Preference tuning
- Reasoning
- Distillation
- Discussion


## Paradigm of LLM training

- LLM training: Train LLM to understand language, then tune it for the end task

1. Pretraining
2. Tuning

### Pretraining overview

- Objective function: Predict next token
- Pretraining is highly parallelizable via teacher forcing
- Masked self attention allows the ability to do things in parallel
- Making the loss less dependent on choice of tokenizer
- Cross entropy loss
- Data mixtures, repetition has value
- A lof of thought is put in the data mixture
- `Olmo 3` model architecture for Olmo
- Approx. trillions of tokens (example:  GLM-5 pretrained on ~30T tokens)


### Mid-training

- **Goal**: Strengthen capabilities on targeted higher-quality data

- It aims in injecting knowledge in the tasks that are more aligned to your usecases
- Secondly, training your model to see longer context inputs 
- We pretrain typically for efficiency purposes
- We pretrain based on sequence legths that are order of thousands of token

### Long context training

Idea: Teach model to use information over longer distances

- How?
    - Extending RoPE. e.g. via Yet another RopE extension method (YaRN)
- Curriculum leaning (4K, 32K, 128K, 1M)
- Why this is hard?
    - Hard to get "good" long observations
    - Dependent on serving system

## Supervised finetuning

- Idea: Change the model behavior by tuning its weights

Strategy:
- Collect pairs of input/outputs with desired behavior (aka SFT data)
- Train using next word prediction objective given the input


### Instruction tuning overview

- Goal: "Graduate" the model to being a helpful assistant

- Objective function: Predict the next token given the input

- Data mixtures: Can be both human-written and synthetic data
    - Assistant dialogs
    - Synthetic instructions
    - Maths, reasoning, code
    - Safety alignment