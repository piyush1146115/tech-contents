# Notes related to CKS

## Kubernetes Secure Architecture

### Architecture

Responsibilities 
 - Run container in container engine
 - Schedule containers efficiently
 - Keep contaienrs alive and healthy
 - Allow common deployment techniques
 - Allow container communication
 - Handle volumes

Components:
- kubectl
- etcd
- apiserver
- kubelet (Node)
- Scheduler
- Pods
- Controller Manager
- Cloud manager controller
- Kube-proxy (Node)

The components running on Node are data-plane and the other components are running on control-plane.

### Pod to Pod communication
- Pod to pod communication is managed by CNI
    - Every pod can communicate to every other pod in a cluster
    