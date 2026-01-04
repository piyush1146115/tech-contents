# Overview of Cloud Native Security

The 4 C's of Cloud Native Security are Code, Container, Cluster, and Cloud.

## Infrastructure Security

- Isolate critical applications on separate servers for better security
- Restrict Docker port access with firewall rules and policies
- Apply least privilege to containers and secure Kubernetes dashboard
- Store sensitive data securely using Kubernetes secrets and RBAC
- Ensure Infrastructure security at each stage
- Enhancing security strategies
    - Encrypt etcd storage


## Kubernetes isolation techniques

- Namespace separation
- Network Policies
- Role Based Access control
- Resource Quotas and limits

## Artifact Repository and Image Security

- Don't use images with latest tag in production
- Use `Trivy` or `Clair` like tools in the CI/CD pipeline for security scan
- You can use integrated vulnerability scanning enabled Artifactory like `Jfrog`
- Add image signing to ensure authenticity

## Workload and Application Code Security

- SQL injection attacks
    - Code scanning tools like `SonarQube` help detect such loopholes in codebase
    - Detecting problematic code patterns
    - Mitigating identified risks
- Realtime Security Monitoring:
    - Datadog Application Security Monitoring
- Performance Challenges
    - Security, Monitoring, Control