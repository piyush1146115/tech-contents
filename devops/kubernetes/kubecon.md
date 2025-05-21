# Kubecon talks

## Kubecon EU 2025- London
- [Kubeflow Ecosystem: What’s Next for Cloud Native AI/ML and LLMOps](https://youtu.be/gGP9QdlNr9Y?si=6jjoiNT9-E-IIwX9)
    - Kubeflow is a bridge between cloud and ML ecosystem
    - Kubeflow notebooks 2.0
      - Interactive IDE for Data Scientist
    - Kubeflow Spark Operator
      - Spark ecosystem for Kubernetes
    - Katib
      - Hyperparameter optimization and neural architecture search for LLM fine-tuning
      - Optimizing RAG Pipelines with Katib- https://blog.kubeflow.org/katib/rag/
    - Kubeflow Trainer
      - Kubeflow trainer is responsible for fine tuning and model training
      - Kubeflow trainer framework obtains rapidly supporting for new model training.
      - Give possibilities to support new ML frameworks for external TrainJob consumers
      - 2 main components: TrainJob and Training Runtime
      - Frameworks supported: Pytorch, DeepSpeed, MLX, Tensorflow (In Progress), Hugging Face (In Progress)
    - Arrow cache
      - Distributed data cache at Kubernetes
      - Apache Datafusion + Apache Arrow + Iceberg
    - Kubeflow Python SDK
      - Unified SDK for processing data, train them and optimize
      - Kubeflow SDK - Llama stack
      - Kubeflow Trainer + torchtune
    - Kubeflow Model registry
      - Model registry UI
      - Custom storage initializer
    - Kserve
      - Highly scalable, standard, cloud agnostic model inference platform on Kubernetes for both predictive and generative AI use cases
      


