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
