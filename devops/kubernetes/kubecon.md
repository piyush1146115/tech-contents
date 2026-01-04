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
      
- [Helm 4 You - Matt Farina, SUSE & Andrew Block, Red Hat](https://youtu.be/rdTPbm9f_fc?si=wo4FKRpe9L7Osm_e)
  - Charts v3
  - Better status checking
  - Improve and extend plugin system

- [Demystifying Why the World Is Built on Kubernetes](https://youtu.be/dVM20108SRc?si=7kqeowrUZWydGi_o)
  - Roles
    - User
      - Infrastructure
    - Administrator
      - Container scheduler and easy self-hosting tools
    - Developer
      - A powerful API server
  - Anatomy of a CRD
    - Custom Resource Definition
    - openAPIv3Schema
    - CRDs are definitions
    - And Custom Resources are unassigned action items
  - Controller
    - Controllers are control loops that watch the state of your cluster, then make or request changes where needed
    - Each controller tries to move the current cluster state closer to the desired state
    - Controllers are event driven applications that run as pods in a Kubernetes cluster
    - Controllers watches resources and then manages other resources. Those resources can be on or off the cluster
    - CRDs are there to define your APIs

- [Building a 5* Kubernetes Hotel - Dean Fuller & Rachael Wonnacott](https://youtu.be/ahANKkTT-yo?si=cC3JbOil819H_X-r)
  - Cillium for network management, Karpenter for scaling, and Keyverno for policy management
  - Security, Resilience, Scaling, Capability and Developer experience
  - Don't underestimate the open-source components
  - You can't hide infrastructure
  

- [n-Place Pod Resize in Kubernetes: Dynamic Resource Management Without Restarts - Tim Allclair & Mofi Rahman, Google](https://youtu.be/HuC4k7fmTBk?si=MGP1IlMdk1FL4uQC)