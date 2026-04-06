# System hardening

## Least Privilege Principle

- Limit access to nodes
- RBAC access
- Remove obsolete packages and services
- Restrict network access
- Restrict obsolete Kernal modules
- Identify and fix open ports

## Limiting Node Access

- User Account, Superuser Account, System Accounts, Service Accounts
- Commands `who`, `last`, `id` 
- Add a VPN for accessing the cluster
- `/etc/passwd`, `/etc/shadow` can reveal password to a user who have access to the controlplane nodes
- Delete a user: `userdel bob`
- Delete user from a group: `deluser michael admin`

## SSH Hardening

- ssh <hostname or IP Address>
- ssh <user>@<hostname OR IP address>
- ssh -l <user> <hostname OR IP address>
- Disable ssh into root account: `vi /etc/ssh/sshd_config`
- Disable password based login - only allow ssh access

## Privilege escalation in Linux

- Update the `/etc/sudoers` file to fine-grain user permissions with sudo access
- `grep -i ^root /etc/passwd`

## Remove Obsolete Packages and Services

- Installing the only required packages
- Update the installed packages are updated regularly
- Remove unwanted services
- Check status of a particular service `systemctl status <svc-name>`
- List all the  service `systemctl list-units --type service`
- Stop and disable a service `systemctl stop apache2`, `systemctl disable apache2`
- Remove the package: `apt remove apache2`

## Restrict Kernal Modules

- Modules can be loaded into the kernal by `modprobe` command