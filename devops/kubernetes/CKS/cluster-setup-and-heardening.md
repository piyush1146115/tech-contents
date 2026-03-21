# Cluster Setup and Hardening

## CIS Benchmarks

- Access, Logging, Auditing
- CIS: Center for Internet Security
- CIS CAT tool
- CIS generates a report in HTML format
- CIS benchmark reference doc for Kubernetes has documented hundreds of references for the security best practices

- The Kube-bench tool is a OSS tool from aqua security that can perform automated assessment to check if Kubernetes is deployed as per the security best practices

## Security Primitives

- Password based authentication disabled
- SSH key based authentication
- Secure Kubernetes
    - kube-apiserver
    - Who can access the cluster and what can they do?
    - Who can access:
        - Static token file, Certificates, External Auth Providers - LDAP, Service Accounts
    - What can they do:
        - RBAC authorization, ABAC authorization, Node Authorization, Webhook Mode
- Network Policies

## Authentication

- Different users accessing the cluster: Admins, Developers, End Users, Bots
- There are multiple auth options in the kube-apiserver
- Consider volume mount while providing the auth file in a kubeadm setup

## TLS Certificates

- CA certificates, Root Certificates, Server Certificates
- server certs: apiserver.crt, apiserver.key
- client certs: admin.crt, admin.key, scheduler.crt, scheduler.key, controller-manager.crt, controller-manager.key, kube-proxy.crt, kube-proxy.key, etc
- Only kube apiserver talks to etcd

## Generate Certificates

- Common tools: EASYRSA, OPENSSL, CFSSL
- admin.key: `openssl genrsa -out admin.key 2048`
- admin.csr: `openssl req -new -key admin.key -subj "\CN=kube-admin" -out admin.csr`
- admin.crt : `openssl x509 -in admin.csr -CA ca.crt -CAkey ca.key -out admin.crt`
- kube-api server: apiserver.crt and apiserver.key
    - kubernetes, kubernetes.default, kubernetes.default.svc.cluster.local

## Viwing Certificate Details

- `cat /etc/kubernetes/manifests/kube-apiserver.yaml`
- `openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout`
- `kubectl logs etcd-master`
- `crictl ps -a`
- `crictl logs <container-id>`

## Certificates API

- Create CertificateSigningRequest object to create a CSR
- `kubectl get csr`
- `kubectl certificate approve jane`
- `kubectl get csr jane -o yaml`

## Kubeconfig

- Without kubeconfig file the kubectl command would be something like this `kubectl get pods --server my-kube-plaground:6443 --client-key admin.key --client-certificate admin.crt --certificate-authority ca.crt`
- Kubeconfig file has 3 main sections: `Clusters`, `Contexts`, and `Users`
- `current-user: dev@google`
- `kubectl config view`
- `kubectl config view -kubeconfig-my-custom-config`
- `kubectl config use-context prod-user@production`
- `kubectl config -h`

## API Groups

- `/version`, `/api`, `/apis`
- Core group and Named group
- `/apis`: /apps, /extensions, /networking.k8s.io, /storage.k8s.io, /authentication.k8s.io, /certificates.k8s.io

## Authorizaion Mode

- Node, RBAC, Webhook
- `kubectl can-i create deployments --as dev-user`

## Kubelet security

- All the components between master and worker nodes need to be secured
- Inspect kubelet: `ps -aux | grep kubelet`
- kubelet serves at 10250 port with full access and 10255 port with unauthenticated read-only access
- Any request that comes into kubelet is first authenticated and then authorized
- kube apiserver uses kubelet-cert and kubelet-key to reach to kubelet
- Default auth mode in kubelet is AlwaysAllow, Set it to Webhook to prevent unauthorized access
- There is a configuration in kubelet to set readonlyport to 0. It disables the unauthenticated access to metrics or audit logs by default

## kubectl proxy & port forward

- you can run `kubectl proxy` command on CLI and do curl request to the localhost
- kubectl port-forward service/nginx 28080:80

## Cluster upgrade

- None of the components can be in higher version than the control-plane
- We should upgrade one minor version at a time
- `kubeadm upgrade plan` will run the pre-flight checks and the system check
- `apt-get upgrade -y kubeadm=1.12.0` 
- `kubeadm upgrade apply`
- `apt-get upgrade -y kubelet=1.12.0-00`
- `kubeadm upgrade node config --kubelet-version v1.12.0`
- `systemctl restart kubelet`
- kubeadm doesn't update kubelet automatically, kubelet binary needs to be updated separately
- `sudo systemctl restart kubelet`

## Network Policies

- podSelector/namespaceSelector
- Two types of policies: Ingress and Egress

```yaml
policyTypes:
- Ingress
ingress:
- from:
  - podSelector:
      matchLabels:
        name: api-pod
    namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: prod
  - ipBlock:
      cidr: 192.168.5.10/32
  ports:
  - protocol: TCP
    port: 3306
```