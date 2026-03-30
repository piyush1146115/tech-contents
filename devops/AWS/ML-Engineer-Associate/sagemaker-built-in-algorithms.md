# SageMaker Built-in Algorithms

## SageMaker introduction

- SageMaker is built to handle the entire machine learning workflow
- SageMaker Notebooks can direct the process
    - Notebook instances on EC2 are spun up frrom thee console
        - S3 dta access
        - Ability to spin up training instances
        - Ability to deploy trained models for making predictions at scale
- Processing Jobs
    - Copy data from S3
    - Spin up a processing container
        - SageMaker built-in or user provided
    - Output processed data to S3
- Create a training job
- Training options
    - Built-in training algorithms
    - XGBoost, Hugging Face, Chainer
    - Your own Docker image
    - Custom Pyuthon Tensorflow/ MXNet code
- Deploying Trained Models
    - Save your trained model to S3
    - Can deploy two ways:
        - Persistent endpoint for making individual predictions on demand
        - SageMaker Batch Transform to get predictions for an entire dataset

## SageMaker Input Modes

- S3 File Mode
    - Default: copies training data from S3 to local directory in Docker container
- S3 Fast File Mode
    - Training can begin without waiting to download data
    - Can do random access, but works best with sequential access
- Pipe Mode
    - Streams data directly from S3
    - Mainly replaced by Fast File
- Amazon S3 Express One Zone
    - High performance storage class in one AZ
    - Works with file, fast file, and pipe modes
- Amazon FSx for Lustre
    - Scales to 100's of GB of throughput and millions of IOPS with low latency
    - Single AZ, requires VPC
- Amazon EFS
    - Requires data to be in EFS already, requires VPC

## Linear Learner in SageMaker

- Linear regression
    - Fit a line to your training data
    - Predications based on that line
- Can handle both numeric regression and classification regression
- When we think about regression, we think about numerical problems, not classification. But, linear learner can do both
    - For classification, it use a linear threshold function
    - Can do binary or multi-class
- File and pipe mode both supported
- Preprocessing
    - Training data must be normalized (so all features are weighted the same)
    - Linear learner can do this automatically
    - Input data should be shuffled
- Training
    - Uses Stochastic Gradient Descent
- Validation
    - Most optimal model is selected
- Important Hyperparameter: balance_multiclass weights, Learning_rate, mini_batch_size, target_precision, weight_decay

## XGBoost in SageMaker

- eXtreme Gradient Boosting
    - Boosted group of decision trees
    - New trees made to correct the errors of previous trees
- Can be used for classification and regression
- Models are serizlized and deserialized with Pickle
- Can use as a framework within notebooks
    - Sagemaker.xgboost
- Important Hyperparameters
    - eval_metric
    - scale_pos_weight
    - max_depth

## LightGBM: What's it for?

- Gradient Boosting Decision Tree
    - Kinda like XGBoost
    - Even more likee CatBoost
    - Extended with Gradient-based one-side Sampling and Exclusive Feature Bundling
- Classification, regressions, or ranking problem
- Important HyperParameter
    - Learning_rate
    - Num_leaves
        - Max leaves per tree
    - Feature_fraction
        - Subset of features per tree
    - Bagging_fraction
        - Similar, but randomly sampled
    - Bagging_freq
        - How often bagging is done
    - Max_depth
    - Min_data_in_leaf
        - Minimum amount of data in one leaf; can address overfitting

## Seq2Seq in SageMaker

- Input is a sequence of tokens, output is a sequence of tokens
- Machine Translation
- Text summarization
- Speech to text
- Implemented with RNN's and CNN's with attention
- Important Hyperparameters
    - Batch_size
    - Optimizer_type
    - Learning_rate
    - Num_layers_encoder
    - Num_layers_decoder
    - Can optimize on:
        - Accuracy
            - Vs. provided validation dataset
        - BLEU score
            - Compares against multiple reference translations
        - Perplexity
- Can only use GPU instance types (P3 for example)
- Can only use a single machine for training
