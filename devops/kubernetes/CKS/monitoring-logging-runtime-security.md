# Monitoring, Logging and Runtime Security

## Perform behavior analytics of system calls

- We can use Falco to analyze the syscalls
- Falco needs to interact with the kernal. It uses eBPF for interacting with the kernal
- We can install Falco as a binary in the nodes or we can use daemonsets to use Falco with the nodes

## Use falco to detect threats

- We use falco rules to filter events as anomalies
- Falco uses several rules as default
- Falco rule fields:
    - rule: <Name of the rule>
    - desc: <description of the rule>
    - condition: <when to filter matching the rule>
    - priority: <severity of the event>
    - output: <output to be generated for the event>

## Ensure immutability of Containers at Runtime

```
securityContext:
  readOnlyFileSystem: true
```

## Kubernetes Auditing

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
omitStages: ["RequestReceived"]
rules:
  - namespaces: ["prod-namespace"]
    verb: ["delete"]
    resources:
    - groups: ""
      resources: ["pods"]
      resourceNames: ["webapp-pod"]
    level: RequestResponse
  - level: Metadata
    resources:
    - groups: ""
      resources: ["secrets"]
```

- Flags with kubeadm setup:
    - `--audit-log-path=`
    - `--audit-policy-file=`
    - `--audit-policy-maxage=`
    - `--audit-log-maxsize`
        