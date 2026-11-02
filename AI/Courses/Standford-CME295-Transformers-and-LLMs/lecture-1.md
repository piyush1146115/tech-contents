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
- BOS - Beginning of Sequence
- EOS - End of Sequence
- PAD - Padding

## Word representation

- Token representation : Naive (one-hot) encoding

### Word2Vec

- Learn the representation with Proxy task
- Neural network with a proxy task over billions of words worth of text
- Learns an embedding layer
- One-hot embedding

#### Proxy tasks

The goal of proxy task here is to predicting some words that is in between of some other words.

- CBOW (Continuous bag of words)
- Skip-grap

Example: Suppose there is a sentence: `A cute teddy bear is reading` and the goal of the proxy task is to predict the word `cute` from the word `A`.

The hidden state of the neural network here called network representation. 

One limitation of this approach is: the same word can have multiple meanings. For example: the word `bank` can have different meaning when someone is going to the bank or someone is going to the river bank.


### Recurrent Neural Networks (RNNs)

- First introduced in the 80s
- Class of neural networks where connections form a temporal sequence
- So, here what you're doing is you're not just considering the embeddings of tokens on their own. You're also considering the embedding of the sequence decoded so far. And that allows you to take into consideration the order of the words in the sentence

- Cons: RNN would have trouble remembering the events far in the past. The issue is called long range dependency

### Long short-term memory (LSTM)

- Introduced in the Long short-term memory paper (1997)
- Uses a more structured approach in the cell's hidden state
- It tries to solve the long range dependency problem with adding not only the hidden state, but also another state called the cell state

## History of attention

- Introduced in 2014
- Translation tasks had a real issue with long-term dependencies
- Seq2seq unable to "remember" what input sentence was saying
- The idea is as follows: instead of solely relying on the hidden state to encapsulate the meaning of the sequence that you have seen so far, the idea is to let your model have direct connections from tokens that you have seen in the past in order to predict next token 
- The concept of attention is letting your model draw direct connections from a given token to some tokens in the past

## Overview of Transformer

- Introduced in the `Attention is All you need` paper, published in 2017
- Relies on the self-attention mechanism
- State-of-the-art results on machine translation tasks

### Concept of Query, Key, Value

- Query: It is the entity trying to determine what a given token is about. The idea is it wants to find tokens that are useful in order to construct a meaningful representation of the token that it is responsible for. Once it determines the magnitude at which it is similar to each token, we will associate a value to each of these tokens
- Sum(i){q,k}
- Now the next question is how do you obtain those? how do you obtain query, key, values
- So these are actually quantities that you can learn with projection matrices. You initially have some input tokens that represent each token. You take that representation, and you project it on the space of queries, of keys, of values through some projection matrices. And you use those quantities in order to compute meaningful representations of tokens
- softmax
- Q.K^T.V (Dot product of Q, transpose of K, and V)

## End-to-end Architecture

- Encoder: Compute meaningful embeddings. The responsibility of the encoder is to compute meaningful representation for the source text that is fed as input
- Decoder: "Generate next token". The role of the decoder is to use the meaningful representation from the encoder along with some internal embeddings that it is computing in order to generate the translation
- Transformers are foundation of modern day LLMs

### Encoder input

- Text is "tokenized"
- Each token has a learned embedding
- Parameters
    - V: vocabulary size
    - d_model: embedding dimensions


### Positional encoding

Idea:
- Add position information to inputs
- Can be either_learned or hardcoded

How do you obtain positional embedding??
- One way is to learn the embedding
- The second way is something that is a function of just different frequencies. The idea is to having a vector of elements tht vary with different frequencies. So you can obtain them with Cosine and Sine functions

### Encoder components

- Encoder-encoder attention / self-attention
    - Self-attention layer computes representation of tokens as a function of all other tokens. And this is where the Query, key, value thing happens. The idea is to learn projection matrices that will allow you to project your tokens into a space of queries, keys, and values, that will then allow them to interact through the formula we saw [Q.K^T.V (Dot product of Q, transpose of K, and V)]. So that allows to represent your tokens as a function of others
- Feed forward neural network
    - Is a way for your architecture to project representations into spaces of higher dimension, along with some activation function, which allows you to learn nonlinearities. 
- Normalization layer

#### Parameters

- N: Layers stacked
- h: number of attention heads
- d_FF, d_key, d_value: sub-layer dimension
- d_model: embedding dimensions



### Decoder input

- Learned embeddings of output tokens
- In practice, will start with [BOS- beginning of sequence] during translation

#### Parameters

- V: vocabulary size
- d_model: embedding dimensions

### Decoder components

- Decoder-decoder attention/self-attention
- Encoder-decoder attention
    - This attention layer is actually letting the representations from tokens that were generated so far and let them interact with tokens from the source, from your input source.
    - In summary, this layer tries to answer this question: how can I express this token as a function of all tokens in the input text
- Feed forward neural network
- Normalization layer
 


### Parameters

- N: layers stacked
- h: number of attention heads
- d_FF, d_key, d_value: sub-layer dimension
- d_model: embedding dimensions

### Decoder outputs

- Linear projection
- Classification problem that outputs probability of belonging to a class, where class=word

#### Parameters

- V: vocabulary size
- d_model: embedding dimensions

### Computational trick: residual connections

Idea:
- Token from te `ResNet paper`
- Element-wise addition of input and output features at different stages of the network
- y=f(x)+x, instead of y=f(x)

Benefits:
- Diversifies features at each level of the network
- Helps with gradient propagation

### Computational trick: layer normalization

Idea:
- Normalize activation outputs over neurons of a hidden layer
- Keeps scale of activations consistent across layers

Benefits:
- Helps with gradient propagation
- Faster, more stable convergance in practice

### Computational trick: masking

- "Masked" also known as "casual" self-attention

Idea:
- Future tokens to be decoded need to be hidden at training time
- Create matrix of masked tokens at each decoding step

Benefit: All operation are vectorized


### Computational trick: multi-head attention

Idea: Run multiple self-attention layers in parallel

Benefits:
- Enables the model to capture different attention features in parallel
- Comparison: multiple filters of a convolutional layer in computer vision

### Computational trick: Dropout

Idea: Randomly drop neural net connections/units with a small probability

- Better generalization

### Computational trick: Label smoothing

Idea:
- 2015 vision paper: overconfidence is bad
- Introduce noise in true labels

Benefits:
- General technique that prevents overfitting
- Improves accuracy and BLEU score

