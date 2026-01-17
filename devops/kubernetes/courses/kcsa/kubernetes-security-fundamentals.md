# Kubernetes Security Fundamentals

## Pod Security Admission and Pod Security Standards
- Pod Security Admission
    - Run this command to check if PSA is available: `kubectl exec -n kube-system kube-apiserver-controlplane -it -- kube-apiserver -h | grep enable-admission-plugins`
    - PSA is configured on namespace level
    - Three profiles are available: Priviledged, Baseline, Restricted
    -  Privileged is unrestricted, Baseline is minimally restricted, Restricted is heavily restricted policy
    - Mode: enforce, audit, warn
        - enforce: Reject pod
        - audit: Record in the audit logs
        - warn: Trigger user-facing warning
    - `kubectl label ns payroll pod-security.kubernetes.io/enforce=restricted`
        - Applying enforce Mode and restricted privelege

```
kubectl label ns beta \
pod-security.kubernetes.io/enforce=baseline \
pod-security.kubernetes.io/warn=restricted
```

```
apiVersion: admissionregistration.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: PodSecurity
    configuration:
      apiVersion: pod-security.admission.config.k8s.io/v1
      kind: PodSecurityConfiguration
      defaults:
        enforce: baseline
        enforce-version: latest
        audit: restricted
        audit-version: latest
        warn: restricted
        warn-version: latest
      exemptions:
        usernames: [] 
        runtimeClassNames: [] 
        namespaces: [my-namespace]  
```

## Authentication

- Auth Mechanisms- Basic
    - Edit the kube-apiserver static pod configured by kubeadm to pass in the user details. The file is located at /etc/kubernetes/manifests/kube-apiserver.yaml
    - kube-apiserver `--basic-auth-file=user-details.csv`
    - kube-apirserver `--token-auth-file=user-token-details.csv`
    - The above methods are very basic and not recommended for production

## Authorization

- ABAC & RBAC
- Node
- Webhook: OPA and other providers
- AlwaysAllow
- `--authorization-mode=Node,RBAC, Webhook`

## RBAC

- Create a Role object
    - Role has rules those contain `apiGroups, resources and verbs`
- Create a RoleBinding object
- To view the roles, run this command: `kubectl get roles`
- To check access: `kubectl auth can-i create deployments` 
- Impersonate other users while checking access:  `kubectl auth can-i create deployments --as dev-user`

a sample Role:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
    name: developer
rules:
-  apiGroups: [""]
   resources: ["pods"]
   verbs: ["get","create","update"]
   resourceNames: ["blue","orange"]
```