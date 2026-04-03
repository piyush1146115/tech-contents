# Generative AI Model Fundamentals

## The transformer architecture

- The evolution of transformer
    - RNNs, LSTMs
    - Introduced a feedback loop for propagating information forward
    - Useful for modeling sequential things
        - Time series
        - Language! A sequence of words
    - Machine translation
    - Encoder/decoder architecture
    - Encoders and decoders are RNN
    - But, the one vector tying them together creates an information bottleneck
        - Information from the start of the sequence may be lost
- Attention is all you need
    - A hidden state for each step (token)
    - Deals better with differences in word order
    - Starts to have a concept of relationships between words
    - But RNN's are still sequential in nature, can't parallelize it
    - Attention weights
- Transformers:
    - Ditch RNN's for feed-forward neural networks (FFNN's)
    - Use "self-attention"

## Self Attention

- Each encoder or decoder has a list of embeddings (vectors) for each token
- Self-attention produces a weighted average of all token embeddings. The magic is in computing the attention weights
- Three matrices of weights are learned through back-propagation
    - Query (Wq)
    - Key (Wk)
    - Value (Wv)
- Every token gets a query(q), key(k), and value(v) vector by multiplying its embedding against these matrices
- Compute a score for each token by multiplying (dot product) its query with each key
- Dot product is just one similarity function we can use
- Repeat entire process for each token (in parallel)
- Now we have our updated embeddings for each token!
- These weight each token embedding as it's passed into the feed-forward neural network

## Application of Transformers

- Chat
- Question answering
- Text classification
- Named entity recognition
- Summarization
- Translation
- Code generation
- Text generation
    - automated customer service

## From transformers to GPT

- GPT: Generative pre-trained transformers
- Decoder only - stacks of decoder blocks
    - Each consists of a masked self-attention layer, and a feed forward neural network
- No concept of input, all it does is generate the next token over and over
    - Using attentions to maintain relationships to previous words/token
    - You prompt it with the tokens of your questions
    - It then keeps on generating given the previous token
- Getting rid of the idea of inputs and outputs is what allows us to train data on unlabeled piles of text
- Hundreds of billions parameters
- Tokenization, token encoding
- Token embedding
    - Captures semantic relationships between tokens, token embeddings
- Positional encoding
    - Captures the position of the token in the input based on other nearby tokens
    - Uses an interleaved sinusoidal function so that it works on any length
- The stack of vectors output a vector at the end
- Multiply this with the token embeddings
- This gives you probabilities of each token being the right next token in the sequence
- You can randomize things here with temperature, instead of always picking the highest probability 