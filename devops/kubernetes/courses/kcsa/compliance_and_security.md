# Compliance and Security Frameworks

## Compliance Frameworks

- GDPR
    - General Data Protectin Regulation
    - It's a EU regulation
    - Secure user data
    - Encrypt user data at rest stored in MySQL
    - Ensure only authorized backend services can access
    - Tools: OneTrust
- HIPAA
    - Health Insurance Portability and Accountability Act
    - HIPAA is US regulation
    - Encrypting PHI stored in and transmitted through Kubernetes
    - Ensuring RBAC is in place for accessing sensitive data
    - Securely configuring Kubernetes secrets for application use
    - Tools: Compliancy Group or Paubox
- PCI
    - Payment Card Industry Data Security Standard
    - Ensure the protection of Cardholder data
    - Applicable throughout the development
    - Tools: Prisma Cloud
- NIST
    - National Institute of Standards and Technology (NIST)
    - Originated in US, but is reconnized globally
    - Conducting regular risk assessments to identify potential vulnerabilities
    - Implementing security controls like firewalls
    - Regular security audits
    - Most applicable during vulnerability assessments
    - Tools: NIST SRE Toolkit
- CIS 
    - Center for Internet Security
    - It's a secruty benchmark
    - Kubernetes components
    - Authentication and Authorization
    - Logging and monitoring
    - Pod security
    - Tools: Kube-bench by aqua security

## Threat Modeling Framework

- STRIDE
    - Developed by Microsoft
    - It helps prevent 6 kind of threts
    - S: Spoofing
    - T: Tampering
    - R: Repudiation - Claiming you didn't do something, where you actully did
    - I: Information disclosure
    - D: Denial of service
    - E: Elevation of Privilege
- MITRE ATTACK
    - Globally accessible resource
    - Initial access: How attackers enter the cluster, such as exploiting weak authentication
    - Persistence: Running unauthorized commands or code, like deploying malicious containers
    - Privilege Escalation: Gaining higher access, such as exploiting misconfigured RBAC
    - Defence Evasion: Hiding activites, like disabling logs or concealing workloads
- Microsoft Threat Matrix for Kubernetes

## Supply Chain Compliance

- Artifacts
    - Verifying what you deploy 
    - Tools: Cosign - signing and verification 
- Metadata
    - Understanding what's inside
    - SBOM
    - Tools: syft
- Attestations:
    - SBOM and other metadata are signed to ensure trustworthiness
    - `cosign verify-attestations ..`
    - Tools: in-toto
- Policies:
    - Ensure compliances and policies are maintained automatically
    - Admission controllers verify these signatures and enforce compliance before deployment

## Automation and Tooling

- `Cloud Native Security Whitepaper` by Sig security is a top resource in the cloud native security world
- Lifecycle: Develop, Distribute, Deploy, Runtime
- Goal of the whole lifecycle is to identify the security issues as early as possible
- Develop:
    - One of the tools that can be used while developing code `oss-fuzz`. Catch vulnerabilities with fuzz testing
    - `Snyk-code` scans code and reports vulenrabilities inside code. 
    - `fabric8` by redhat that provides insights about code 
    - `kube-linter` analyzes potential issues in kubernetes yeaml files
- Distribute:
    - CI/CD, Containerization, Pushing/pulling from 
    - Build Pipelines: Tekton, Jenkins, Travis CI, FluxCD, ArgoCD
    - Container Registry: Docker, Distribution, Harbor, GIthub Registry, Nexus Repository
    - Kubesec, terrascan: Scans the manifests file of deployable resources
    - Nuclei, Trivy, Snyk Container, Clair, Grype are comprehensive and static security scanners for image or binaries against vulnerabilites or compliance
    - Signing/trust: in-toto, notation, Tuf, sigstore
- Develop:
    - Preflight checks: Gatekeeper, Kyverno. They define policies and validate requests before getting deployed
    - Observabiluty: Prometheus, Grafana, Elastic, Kibana. Opentelemetry
    - Response and Investigation: Wazuh, Snort, Zeek
- Runtime:
    - Orchestration: kube-bench, Trivy, Falco, Spiffe
    - Service Mesh: Istio, Linkerd
    - Storage: Rook, Ceph, Gluster
    - Access: Keycloak, Teleport, Hashicorp Vault