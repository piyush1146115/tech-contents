# Kubernetes Threat Model


## Persistence

Persistence means the ability of a attacker to maintain access to an compromized system even after reboot, update, interruptions etc.

- Persistence allows attackers to maintain access in clusters
- Attackers read secrets and leverage misconfigurations for persistence
- Restrict RBAC permissions to prevent unauthorized access
- Secure secrets management to protect sensitive information
- Harden pod security to limit attack impact

## Denial of Service

- DoS attacks overwhelm system resources, causing unresponsiveness
- Set resource quotas to prevent excessive resource usage
- Restrict service account permissions to limit potential attacks
- Use Network Policies and firewalls to control access
- Monitor and alert on unusual activity for quick response


## Malicious code execution

- Attackers exploit vulnerabilities in containers to execute malicious code
- Restrict API server access to authorized users and services only
- Secure image repositories and use signed images for verification
- Regularly update and patch applications to prevent security exploits

## Compromised Container Attack Tree

- Push poisoned image to image repository
- Exfiltrate imagae from image repository

## Attacker on the Network

- Attackers can target Kubernetes control plane and nodes for breaches
- Configure firewalls to limit network access to trusted IP addresses
- Keep node operating systesms and components updated and patched
- Implement network policies to control traffic and prevent lateral movement
- Use strong authentication, multi-factor, and RBAC for secure access
- Monitor and log activieties to detect and respond to threats

## Access to Sensitive Data

- Ensure RBAC permissions are correctly configured to avoid excessive access
- Secure logs to prevent storing and exposing sensitive information
- Encrypt network traffic using TLS to prevent eavesdropping attacks

## Privilege Escalation

cat /etc/sudoers

```
User privilege specification

root ALL=(ALL:ALL) ALL

```