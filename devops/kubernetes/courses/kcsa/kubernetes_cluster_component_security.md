# Kubernetes Cluster Component Security

## API Server

## Controller Manager and Scheduler

Kubernetes controller manager and scheduler manager are cruicial for managing Kubernetes task. 

- Isolate Controller Manager and Scheduler on separate dedicated nodes 
- Use RBAC to ensure the permission escalation is not possible
- Ensure TLS from node to control-plane components
- Enable Audit logging for all components
- Secure default settings and protect the configuration files
- Run the latest version of Kubernetes

## Securing the Kubelet

Kubelet does the following job in a node:
- Register node with kube apiserver
- Create Pods
- Monitor Node and Pods

- Kubeadm does not deploy kubelets, kubelets need to be manually installed
- Kubelet has a configuration file which stores the necessary configuration for starting kubelet service
- View kubelet options: `ps -aux | grep kubelet`
- Kubelet has two ports:
    - Port 10250 serves API that allows full access
    - Port 10255 serves API that allows unauthenticated read-only access

Securing Kubelet:
- Disable anonymous authentication in kubelet configuraiton
- Use TLS in APiserver to Kubelet communication
- Enable Authorizaton webhook
- Kubelets support two kinds of authentication: certificate based authentication and token based authentication


## Securing container runtime

- Keep your container runtime updated to fix vulnerabilities. Update with security patches regularly
- Run containers with least privileges to minimize security risks
- Limit resource usage like memory and CPU
- Use security profiles
- Use monitoring and logging
- Enable audit logs

## Securing Kube Proxy

- Get the kube-proxy process details by `ps -ef | grep kube-proxy`
- Check the file permission of Kube-proxy config: `stat -c %a /var/lib/kube-proxy/kubeconfig.conf`

- Secure kube-proxy config file with strict permissions
- Encrypt API server communication using TLS and Service Accounts
- Run kube-proxy with least privileges necessary
- Implement network policies for traffic control
- Use logging and monitoring for detecting anomalies
- Enable audit logs


## Pod Security

- Pod Security Policy was removed from version 1.25
- As an alternative, Pod Security Admission and Pod Security Standards came into the picture
- There was a pod security admission controllers 
- Pod security policy could validate and mutate Pod creation requests
- 

