# Kubernetes Threat Model


## Persistence

Persistence means the ability of a attacker to maintain access to an compromized system even after reboot, update, interruptions etc.

- Persistence allows attackers to maintain access in clusters
- Attackers read secrets and leverage misconfigurations for persistence
- Restrict RBAC permissions to prevent unauthorized access
- Secure secrets management to protect sensitive information
- Harden pod security to limit attack impact