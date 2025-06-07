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

### Public Key Infrastructure in Kubernetes - Certificate Authority - CA
  - CA is the trusted root of all certificates inside the cluster
  - All cluster certificates are signed by the CA
  - Used by components to validate each other
  - CA signs the following certs:
    - apiserver cert
    - kubelet cert
    - scheduler cert
  - We'll look to find certificates
    - CA
    - Api server cert
    - Etcd server cert
    - API -> Etcd
    - API -> kubelet
    - Scheduler -> API
    - Controller manager -> API
    - Kubelet -> API
    - Kubelet server cert

```
root@cks-master:~# ll /etc/kubernetes/pki
total 68
drwxr-xr-x 3 root root 4096 May 31 20:30 ./
drwxrwxr-x 4 root root 4096 May 31 20:30 ../
-rw-r--r-- 1 root root 1123 May 31 20:30 apiserver-etcd-client.crt
-rw------- 1 root root 1679 May 31 20:30 apiserver-etcd-client.key
-rw-r--r-- 1 root root 1176 May 31 20:30 apiserver-kubelet-client.crt
-rw------- 1 root root 1679 May 31 20:30 apiserver-kubelet-client.key
-rw-r--r-- 1 root root 1285 May 31 20:30 apiserver.crt
-rw------- 1 root root 1679 May 31 20:30 apiserver.key
-rw-r--r-- 1 root root 1107 May 31 20:30 ca.crt
-rw------- 1 root root 1675 May 31 20:30 ca.key
drwxr-xr-x 2 root root 4096 May 31 20:30 etcd/
-rw-r--r-- 1 root root 1123 May 31 20:30 front-proxy-ca.crt
-rw------- 1 root root 1679 May 31 20:30 front-proxy-ca.key
-rw-r--r-- 1 root root 1119 May 31 20:30 front-proxy-client.crt
-rw------- 1 root root 1679 May 31 20:30 front-proxy-client.key
-rw------- 1 root root 1679 May 31 20:30 sa.key
-rw------- 1 root root  451 May 31 20:30 sa.pub
```

Check out kubelet, controller manager and scheduler conf.
```
root@cks-master:~# vim /etc/kubernetes/scheduler.conf
root@cks-master:~# vim /etc/kubernetes/controller-manager.conf
root@cks-master:~# vim /etc/kubernetes/kubelet.conf


root@cks-master:~# ll /var/lib/kubelet/pki
total 20
drwxr-xr-x 2 root root 4096 May 31 20:30 ./
drwxrwxr-x 9 root root 4096 May 31 20:30 ../
-rw------- 1 root root 2826 May 31 20:30 kubelet-client-2025-05-31-20-30-58.pem
lrwxrwxrwx 1 root root   59 May 31 20:30 kubelet-client-current.pem -> /var/lib/kubelet/pki/kubelet-client-2025-05-31-20-30-58.pem
-rw-r--r-- 1 root root 2283 May 31 20:30 kubelet.crt
-rw------- 1 root root 1675 May 31 20:30 kubelet.key
```

### Kernal vs User Space

- Applications -> Libraries -> Syscall Interface -> Linux kernal -> Hardware
- Containers vs VM:
    - VM doesn't share the same kernal
    - Containers share the same kernal in different groups
- Linux Kernal Namespaces:
  - Namespaces isolate processes
  - Containers are simply processes on kernal, isolated by namespaces
  - Process ID 10 can exist multiple times, once in every namespace
  - Restrict access to mounts or root file system
  - Only access certain network devices
  - Firewall and routing rules & socket port numbers
  - Not able to see all traffic or contact all endpoints
- Namespaces restrict what processes can see: other processes, users, and filesystem
- Cgroups restrict the resource usage of processes


## Container tools

- Docker: Container runtime + Tool for managing container and images
- ContainerD: Container Runtime
- Crictl: CLI for CRI-compatible Container Runtimes
- Podman: Tool for managing containers and images