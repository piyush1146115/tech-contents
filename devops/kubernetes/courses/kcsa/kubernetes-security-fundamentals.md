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

```yaml
kind: Role
metadata:
  creationTimestamp: "2026-01-18T19:47:41Z"
  name: kube-proxy
  namespace: kube-system
  resourceVersion: "289"
  uid: 7c1cf051-37c1-4e6b-a271-66c4a3ce8865
rules:
- apiGroups:
  - ""
  resourceNames:
  - kube-proxy
  resources:
  - configmaps
  verbs:
  - get
```

```bash
kubectl create role developer --namespace=default --verb=list,create,delete --resource=pods
```
## Secrets

Secrets are used to store sensitive information. 

There are two ways of creating a secret:
- imperative: `kubectl create secret generic --from-literal/--from file`
- declarative: kubectl create -f

- To encode data to base64: `echo -n 'mysql' | base64`

## Isolation and Segmentation - Namespace

- Automatic namespaces: `kube-system`, `default`, and `kube-public`
- Namespace-  limit resources with ResourceQuota
- kubectl get pods -n <namespace-name>
- `kubectl config set-context $(kubectl config current-context) --namespace=dev`

## Isolation and Segmentation - Resource Quotas and Limits

- Requests and Limits
- LimitRange resource help you define default resources for Pods/.This is applicable in namespace level

```yaml
apiVersion: v1
kind: LimitRange
metadata:
    name: cpu-resource-constraint
spec:
    limits:
    - default:
        cpu: 500m
      defaultRequest:
        cpu: 500m
      max:
        cpu: "1"
      min:
        cpu: 100m
      type: Container
```
- ResourceQuota resouces for limiting resouces in a namespace

## Audit Logging

- Audit Policy

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
omitStages: ["RequestReceived"]
rules:
    - namespaces: ["prod-namespace"]
      verbs: ["delete"]
      resources:
      - groups: " "
        resources: ["pods"]
        resourceNames: ["webapp-pod"]
      level: RequestResponse
```

- `--audit-log-path=/var/log/k8-audit.log`
- `--audit-log-maxsize=10`

## Network Policy

- PolicyTypes: Ingress/Egress
- Selectors: podSelector, namespaceSelector, ipBlock