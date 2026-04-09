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
- Run `lsmod` to check running kernal modules

## Identify and Disable Open Ports

- To check on the ports making connection request: `netstat -an | grep -w LISTEN`
- https://www.cisecurity.org/cis-benchmarks/
- https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#check-required-ports

## Minimize IAM Roles

- Least Privilege in Cloud IAM policies like AWS
- IAM Group like Developer, Admin etc
- Add users to the relevent groups
- AWS Trusted Advisor tool in AWS. Similar tools available in GCP and Azure

## Restricting Networrk Access

## Uncomplicated Firewall (UFW)

- `netstat -an | grep -w LISTEN`
- `ufw status`
- `ufw default allow outgoing`
- `ufw default deny incoming`
- `ufw allow from 172.16.238.5 to any port 22 proto tcp`
- `ufw enable` to enable the firewall
- `ufw deny 8080`
- `ufw status`

## Linux Syscalls

- To see how a command works in kernal syscall: `strace touch /tmp/error.log`
- To check the pid of a process, run this command: `pidof etcd`
- To see all the syscall by a command, add `-c` flag: `strace -c touch /tmp/error.log`

## Aquasec Tracee

- Tracee uses eBPF to monitor the syscalls
- Tracee needs access to kernal headers
- To observe the syscalls by a single command: 
- To observe all the processes on the host: `sudo docker run --name tracee --rm --privileged --pid=host -v /lib/modules/:/lib/modules/:ro -v /usr/src:/usr/src:ro -v /tmp/tracee:/tmp/tracee aquasec/tracee:0.4.0 --trace pid=new`

## Restricting Syscalls Using Seccomp

- Currently there are about 435 Syscalls in Linux
- Having access to all syscalls from an app can increase the attack surface
- To check if seccomp is supported by the kernal: `grep -i seccomp /boot/config-$(uname -r)
- `{"defaultAction": "", "syscalls":[{names:[]"action": ""}] }`
- 