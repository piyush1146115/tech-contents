# Minimize Microservice Vulnerabilities

## Admission Controllers

- `kubelet -> Authentication -> Authorization -> Create pod`
- With Admission Controllers: `kubelet -> Authentication -> Authorization -> Admission Controllers -> Create pod`
- Admission controllers example: AlwaysPullImages, DefaultStorageClass, EventRateLimit, NamespaceExists
- To see the list of enabled Admission controllers: `kube-apiserver -h | grep enable-admission-plugins`
- Update the kube-apiserver manifest file in the `/etc/kubernetes/manifests/kube-apiserver.yaml` to enable new admission plugins

## Validating and Mutating Admission Controllers

- Mutating Admission Controllers can change the request
- Validating Admission Controllers validate the API requests
- Any rejected requests by validating admission controllers shows an error message to the users
- User defined webhooks: `MutatingAdmission Webhook` and `ValidatingAdmission Webhook`
- Steps to have a custom webhook:
    - Deploying a Webhook server with custom implementation logic in Golang, Python, etc
    - Configuring Admission Webhook

## Pod Security Policy

```yaml
kind: Pod
spec:
  containers:
    - name: ubuntu
      image: ubuntu
      command: ["sleep", " 3600"]
      securityContext:
        privileged: True
        runAsUser: 0
        capabilities:
            add: ["CAP_SYS_BOOT"]
```

- Pod Security Policy was replaced by `Pod Security Admission` and `Pod Security Standards`

## Pod Security Admission and Pod Security Standards

- There are 3 modes in the the security standards
    - Privileged: Unrestricted policy
    - Baseline: Minimally restrictive policy
    - Restricted: Heavily restricted Policy
- Mode specify the actions on the policy violations:
    - enforce: Reject Pod
    - audit: Record in audit logs
    - warn: Trigger user-facing warning
- <mode>=<security-standard>
- `kubectl label ns payroll pod-security.kubernetes.io/enforce=restricted`
- `kubectl label ns hr pod-security.kubernetes.io/enforce=baseline`

## Open Policy Agent

- OPA installation
- Load policy in OPA. The file containing policies has `.rego` extention
- Rego is a policy language. There are playgroud to test the policies online

## OPA in Kubernetes

- OPA Constraint Framework
    - What? - What requirements do I have?
    - Where? - Where do I want to enforce the requirements?
    - How? - How do I specify what to check and what action to take?

## Manage Kubeernetes secrets

- Secrets can be created imperatively and declaratively
- encode "echo -n 'mysql' | base64"

## Encrypting Secret Data at Rest

- etcdctl --cacert= --cert= --key= get /registry/secrets/default/secret1 | hexdump -C
- First check if encryption is already enabled: `ps -aux | grep kube-api | grep "encryption-provider=config"` or `vi /etc/kubernetes/manifests/kube-apiserver.yaml`
- 
```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
    - resources:
        - secrets
      providers:
        - aesbc:
            keys:
                - name: key1
                  secret: y0x...
        - identity: {}
```

## Container Sandboxing

- Sandboxing refers to any technique that isolate a setup from rest of the system

## gVisor

- gVisor ensures an additional level of isolation from the container to kernal of host system
- container -> syscall -> gvisor (Sentry <-> Gofer) -> Limited syscalls

## kata containers

- kata creates lightweight VMs
- To run Kata containers in cloud, we need support of nested virtualization

## Container runtime

- To run a container docker/containerd requires a container runtime. It's `runc` for both of them
- Runtime requires to be oci compatible
- There are other runtime available as well like kata-runtime, Runsc (gVisor)
- For OCI compatibility we can use other runtime with docker
- `docker run --runtime runsc -d nginx`

## Runtime Class in Kubernetes

```yaml
apiVersion: node.k8s.io/v1beta1
kind: RuntimeClass
metadata:
    name: gvisor
handler: runsc

```

To specifically instruct the pod to use the gVisor runtime:

```yaml
apiVersion: v1
kind: Pod
metadata:
    labels:
        run: nginx
    name: nginx
spec:
  runtimeClassName: gvisor
  containers:
  - image: nginx
    name: nginx
```