# Lecture 2: Transformers and Large Language Models

Link: https://www.youtube.com/watch?v=GaIeu3npx04&list=PPSV&t=5s

- Recap of last lecture
    - How to divide our text into indivisible units = tokenizatin
    - Subword tokenization is most popular method
    - Transformer architecture
    - Encoders and decoders
    - Query, key, value

## Contents

- Transformer model families
- Scaling laws
- Expert routing
- Architecture optimizations
- Decoding strategies
- Prompting and reasoning




## Transformer Architecture

- Encoder + Decoder
- Encoder = "Compute meaningful embeddings"
- Decoder = "Generate next token"


- What if we only try with Encoder?
    - BERT = Bidirectional Encoder Representations from Transformers
        - Idea: Leverage encoded embeddings with multi head attention layer which performs self-attentions operation over all of its inputs to make predictions
        - CLS token: Classification token

## BERT and encoder-only models

- Strategy:
    - Step 1: Pretraining with proxy tasks: Masked Language Model (MLM)
    - The model tries to understand how language is written and trying to understand what are the words that are likely to be in places where it is missing
    - Step 1: Pretraining with proxy tasks: Next sentence prediction (NSP)
        - The idea behind this proxy task is for the model to understand how sentences are sequenced
        - The idea behind the proxy task is for the model to learn text, not at the sentence level, but at the document level
    - Step 2: Finetuning for given end task
        - The second task is for you to adapt your model to the specific use case that you're interested in
- Pros:
    - Good performance
    - Finetuning does not need a lot of data
- Cons:
    - Finetuning is a required step
    - Not suited for a range of tasks


## Transformer variant: decoder-only


### GPT = Generative Pre-trained transformer

Idea: Predict next token one at a time

- The idea is to only keep the decoder parts of the transformer and formulates any task you have as a text-to-text problem
- That means you have some text as input, and your only job is to predict the next token
- This is called auto-regressive decoding. Because you predict tokens one at a time


### Encoder-decoder versus decoder-only

- Both are similar in that they can generate text
- But in the case of encoder-decoder architecture, the input has a special treatment. Within the encoder all the tokens are able to interact with one another
- Whereas in decoder-only architecture, what you have as input, the tokens can only interact between themselves and tokens before them. They can not interact with tokens after them.
- Bidirectional attention in encoder-decoder model for the inputs
- Causal attention in decoder-only model for the inputs
- Decoder only architecture is a little bit more general as this treats everything the same
- People have tried both approaches when it came to the text-to-text paradigm, and overwhelmingly they pretty much all went with the decoder only.
- One of the reasons of picking up decoder only model is it is simpler and requires no special treatment of the inputs. You don't need an encoder to treat the input separately

## Scaling laws

- In the early 2020s, there were a couple of papers that actually quantified how much better your model was getting as you were training it on more data, with more parameters, with more compute
- `Scaling laws for natural language models`, Kaplans et el
- Better performance with bigger models and more data
- Bigger models are more token efficient. They need fewer tokens to perform better.
- As you can imagine, the hardware is limited
- Paper: `Training compute-optimal large language models, Hoffmann et al, 2022`
- Chinchila law: takeways on compute-optimal training


### Some notations

- FLOPs = Floating-point Operations
    - The higher the FLOPs, the more compute you actually have
    - Training FLOPs for LLMs is like 10^25
- FLOP/s = Floating point operations per second
    - This is actually the compute speed
    - It's a measure of how performant your hardware is

## LLM = Large Language Model

- A language model is a statistical or machine learning model that assigns probabilities to sequences of tokens
- Why it is called large
    - Model size: billions of parameters or more
    - Training data: 100s of billions of tokens or more
    - Compute: a lot of GPUs
- Decoder-only Transformer based model
- The backbone of this architecture is a causal multi-head attention layer, which is only attending to each token and the tokens that came before it and a feed forward neural network
- Examples: GPT series, Gemma, Deepseek, Qwen, GLM, Kimi


### Overview of MOEs

MOE = Mixture of Experts

- Dense MoE: Output is weighted average of all expert outputs
- Sparse MoE: Output is weighted average of selected expert options

### MoE in transformer-based models

- Where would you put the MoE scheme in the decoder architecture?
    - So the answer here is you can take a token and project it in order to select which expert it is. That is the role of the router. 
    - The answer would be Feed forward neural network
    - The router decides which expert needs to be activated and the expert itself is a feed forward neural network
    - How does the router know when to activate each expert? -> the magic of back propagation. 

### Training challenges include routing collapse

Symptom: Same expert gets selected most of the time. this is called "routing collapse"

Remedy: Force other experts to be "part of the game" too via auxilary loss

- The routing is done at token level

- fi = fraction of tokens routed to expert i
- Pi = average routing probability for expert i

- Training a MoE based LLM is challenging


### Recent trends

- Shared experts to minimize redundant information between experts
- Fine-grained experts with top k > 1
- Orders of manitude among frontier open-source models: the number of experts they have on average is on the order of 100s. For example: MiMo-v2.6Pro: 384, GLM-5: 256, DeepSeek V4.1 Flash: 384
- Number of experts activated in a typical forward pass is 8 or so
- In terms of models size, they are 100s of billions of parameters


## Architecture optimizations


### Hardcoded position embeddings

Idea: Hardcode values of position embedding

- The idea behind the deterministic formulation is to express each position on a high dimensional vector. What you want it that vector to exactly inform you in which position you are in. You also want two positions to be embedded, such that the similarity operation between these two embeddings are high if the positions are close and it's low when these positions are far.
- For position embedding, we do something similar like the clock hands
- We have a function of higher and lower frequency such that when you put all of that together into one vector, you know exactly which position you are at
- Higher frequency for lower index and lower frequency fr higher index
- If you have a position M and a position N, how do you calculate the similarity?
    - you take the dot product. Dot product of two vector positions
- Hardcode values of position embedding:
    cos(a-b) = cos(a)cos(b) + sin(a)sin(b)
- The dot product of two embeddings at position m and n is a function of m minus n. Cosine of 0 is the maximum number, that cosine can take. In other word, when m=n the difference would be 0 and the similarity score would be maximum possible
- Positions that are close together are of high similarity and positions that are further together are of lower similarity

### From absolute to relative position info

Idea: Lets change the attention layer instead

#### Linear  bias attention layer

idea: Add bias query-key scores

ALiBi: Bias is linear, deterministic, not bounded

#### Default choice nowadays: RoPE

- **RoPE** = Rotary Position Embeddings

idea: Rotate query and key vectors with rotation matrix

- We are going to rotate key and query, each of them as a function of the position that they are in.
- Why it is something very appealing?
    - Well, because the nice thing is when you rotate the query, when you rotate the key, what you're actually doing, when you do the self attention formula is you're actually bubbling up. 
- Use rotation matrix
- If you multiply your vector with the rotation matrix, you are rotating your vector
- If you rotate your query vector by some angle as a function of it's position m, and you rotate your key vector by some angle as function of it's position n, then you obtain a rotation matrix that is actually a function of n minus m f(n-m).
- It is extensible to any positions
- If you take a look at the order of magnitude of the dot product between query and the key as a function of how far their positions are, then you will see roughly it tends to decay as m and n are farther apart. So, it is not strictly monotonic. At a very high level, it just decays and it just reflects what we want in tokens that are very far apart.
- So in other words, the original transformer paper used position embeddings that were additive, which is in contrast with nowadays where people use RoPE


### Leveraging local and global attention

SWA = Sliding window attentions

- Variations include interleaving local and global attention layers
- Your model is actually not a one block of decoders, it is several blocks. So the attention operation is not just happening once. It is happening several times
- Similar to receptive field in computer vision

### Sharing attention heads

- People have tried saving up the number of keys and the number of values that each token needs to produce
    - Multi query attention (MQA)
    - Group query attention (GQA)
    - Multi-Head Attention (MHA)


### Different kinds of layer normalization

- Post-Norm: Output= LayerNorm(x + SubLayer(x))
- Post-Norm is normalizing after the operation
- People nowadays normalize before the operation and use the Pre-Norm method more
- Pre-Norm: Output = x + SubLayer(LayerNorm(x))

### Layer normalization

- RMSNorm(x)
    - You don't need to recenter x, you just need to rescale it
- Before people were using Post-Norm + LayerNorm
- Nowadays people use Pre-Norm + RMSNorm

- So long story short, nowadays RoPE, local attention, gka GQA, pre-norm and RMS norm

## Next token prediction


### Predicting next token with greedy decoding

- 1st idea: Take token with highest predicted probability

### Predicting next token with beam search

- 2nd idea: Keep k paths that are most likely

### Predicting next token with sampling

- 3rd idea: Sample next token from probability distribution
    - Top-k: Sample among top k most probable tokens
    - Top-p: Random sample among smallest set of tokens with cumulative probability > p

### Probability computation

- In the last layers, you have linear projection between the model and the embedding space of your token at a given time. And then you project it on the space of vocabulary. Based on this, you apply the Softmax operator to convert this numbers into a probability distribution
- Temperature allows a tweak output probabilities

### LLM determinism is hard

- There is a concept of batch invariant. That is not respected in some cases
- Blog: `Defending non-determinism in LLM inference`

### Constraining the output via guided decoding

Idea: Only allow "Valid" next tokens

- The span of available tokens to be predicted at the next step is restricted depending on the syntax of the language you want to decode this in

## Prompting and reasoning

- Context window, it's linked to output tokens as well
    - Industry standard token window is now 1M for input token
        - Example: Opus 5.5 has 1M input and 128k output token, GPT-6.1 Sol has 1M input and 128k output token
- Why you need a fixed context window
- Mental model:
    - 1 token= 0.75 word
    - 1 U.S> letter page with 12pt font text = 400 words
- Orders of magnitude: What can we do with all these tokens?
    - 10,000 tokens: technical report
    - 100,000 tokens: book
    - 1,000,000 tokens: encyclopedia
- Are more tokens the better?
    - Beware of context rot
    - Test: needle in a HayStack

### ICL= In-context learning

- Zero-shot learning
- Few-shot learning

### Chain of thought

Idea: Explaining reasoning helps in improving performance

- Paper `Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, Wei et al, 2022`
