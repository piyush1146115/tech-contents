# Platform Security

## Supply Chain Security - Minimize base image footprint

- Base vs Parent Image
- Build modular images
- Don't persist state inside container

## Scan image

- `trivy image --severity CRITICAL nginx:1.18.0`
-  `trivy image archive-image.tar`

Best practices:
- Continuously rescan images
- Kubernetes Admission Controllers to scan images
- Have your own reository with pre-scanned images ready to go
- Integrate scanning into your CI/CD pipeline

## Image Repository Security

```
kubectl create secret docker-registry regcred \
 --docker-server=private-registry.io \
 --docker-username=registry-user \
 --docker-password=registry-password \
 --docer-email=registry-user@org.com
```

## Observability Overview

- Falco
    - Monitor Syscalls

### Falco Overview

- Policy Engine
- Libraries
- Falco Rules
- Falco Kernal Modules

- Falco rules
    - rule
    - descritption
    - condition
    - output
    - priority


## Service Mesh and Istio

- Monolithic Applications
- Microservice
    - Complex Service Networking
- Service Mesh: It is a dedicated and configurable infrastructure layer that handles thee communication between services without having to change the code in a microservice architecture
- Istio is a free and open-source service mesh
- Istio uses Envoy as the proxy
- Istio control-plane originally consisted of three components: Citadel, Pilot, and Galley
- Citadel managed certificate geenration, Pilot helped with service discovery and Galley helped with validating configuration
- The three components were lated merged into a single daemon called `Istiod`

## Security in Istio

- There is a certificate authority inside Istiod which creates and validates certificates

## K8s PKI - Certificate Creation

- Generate Keys: `openssl genrsa -out ca.key 2048` -> ca.key
- Certificate Signing Request: `openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr` -> ca.csr
- Sign Certificates: `openssl -req -in ca.csr -signkey ca.key -out ca.crt` -> ca.crt

## K8s PKI - View Certificate Details

- cat `etc/kubernetes/manifests/kube-apiserver.yaml`
- `openssl x509 -in /etc/kubernetes/pki/apiserver.crt -teext -nout`
- Inspect service logs: `journalctl -u etcd.service -l`
- docker ps -A 
- docker logs <container-id>

## Connectivity - TLS Basics

- Symmetric Encryption
- Asymmetric encryption
- `ssh-keygen`: id_rsa id_rsa.pub . id_rsa is private key. id_rsa.pub is the public key/lock
- `cat ~/.ssh/authorized_keys` : ssh-rsa AAA... Authorized public keys are stored in the server where access verification is required
- Certificate Authority: Symantec, Digicert, GlobalSign, etc
- Certificate Authorities use their private keys to sign the certificates
- Servers send a Certificate Signing Request (CSR) to the CAs to sign the public cert
- Usually public keys have .crt or .pem extension
- Usually private keys have .key or key.pem extension

## Connectivity - TLS in Kubernetes

- Server Certificates in Kubernetes
    - Kube-API server: apiserver.crt, apiserver.key
    - ETCD Server: etcdserver.crt, etcdserver.key
    - Kubelet Server: kubelet.crt, kubelet.key
- Client Certificates in Kubernetes
    - admin.crt, admin.key
    - scheduler.crt, scheduler.key
    - controller-manager.crt, controller-manager.key
    - kube-proxy.crt, kube-proxy.key
    - apiserver-kubelet-client.crt, apiserver-kubelet-client.key
    - apiserver-etcd-client.crt, apiserver-etcd-client.key
    - kubelet-client.crt, kubelet-client.key
- kubernetes Certificate Authority
    - ca.crt, ca.key


## Connectivity - mTLS

- Client and Server both verifies the authenticity of each other

## Kubernetes Admission Controllers

- Authorization- RBAC
- Admission Controllers give us better security control on how a cluster is used
- Default Admission Controllers in Kubernetes Clusters:
    - AlwaysPullImages: Ensures that every time a pod is created, the image is pulled
    - DefaultStorageClass: Observes the creation of PVCs and automatically assign default storageclss  to them if that's not specified explicitly
    - EventRateLimit: Implement Rate limiting for the events coming to the Api server
    - NamespaceExists: NamespaceExists admission controller rejects the request where the specified namespace doesn't exist
- To see the enabled Admission controllers: 
    -  `kube-apiserver -h | grep enable-admission-plugins`
    - `kubectl exec kube-apiserver-controlplane -n kube-system --kube-apiserver -h | grep enable-admission-plugins`
- To add any new admission controller by default, update the `--enable-admission-plugins` in the kube-apiserver config
- To disable admission controller use the `--disable-admission-plugins` flag
- Kubectl -> Authentication -> Authorization -> Admission Controllers -> Create Pod