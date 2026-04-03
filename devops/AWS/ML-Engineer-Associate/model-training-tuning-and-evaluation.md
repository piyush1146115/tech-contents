# Model training, tuning, and evaluation

## Activation function

- Define the output of a node/neuron given its input signals
- Linear activation function
    - Can't do backpropagation
- Binary step function
    - It's on or off
    - It can not handle multiple classification - it's binary
- Non-linear activation function
    - These can create complex mappings between inputs and outputs
    - Allow backpropagation
    - Allow for multiple layers
    - Example: hyperbolic tangent function, sigmoid logistic
    - Computationally expensive
- Rectified Linear Unit (Relu)
    - Easy and fast to compute
- Softmax: 
    - Used on the final output layer of a multi-class classification problem

## Convolutional Neural Network (CNN)

- What they're for
    - When you have data that doesn't neatly align into columns
    - They can find features that aren't in a specific spot
    - They are "feature location" invariant
- Inspired by the biology of visual cortex
- CNN with keras/tensorflow
    - Source data must be in appropriate dimension/shape
    - Typical usage: Conv2D -> MaxPooling2D -> Dropout -> Flatten -> Dense -> Dropout -> Softmax
- CNN are very compute intensive (GPU, CPU, Memory)
- Lots of hyperparameters

## Recurrent Neural Network

- Time-series data
    - When you want to predict future behavior based on past behavior
- Data that consists of sequences of arbitrary length
    - machine generated music
    - image captions
    - machine translation
- The past behavior of recurrent neuron influences the future behavior and influences how it learns
- RNN topologies
    - Sequence to sequence
        - Example: Predict stock prices from series of historical data
    - Sequence to vector
        - Words in a sentence to sentiment
    - Vector to sequence
        - Create captions from an image
    - Encoder to decoder
        - Sequence -> Vector -> Sequence. Machine translation
- Training RNN
    - Steps from earlier time steps get diluted over time
        - This can be a problem for example learning  sentence structures
    - LSTM cell
        - Long short term memory cell
        - Maintains separate short-term and long-term states
    - GRU cell
        - Gated recurrent unit
        - Simplified LSTM cell, very popular in practice
    - They are very sensitive to hyperparameter choice
    - They are very resource intensive


    
