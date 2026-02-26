# Cluster Setup and Hardening

## CIS Benchmarks

- Access, Logging, Auditing
- CIS: Center for Internet Security
- CIS CAT tool
- CIS generates a report in HTML format
- CIS benchmark reference doc for Kubernetes has documented hundreds of references for the security best practices

- The Kube-bench tool is a OSS tool from aqua security that can perform automated assessment to check if Kubernetes is deployed as per the security best practices

## Security Primitives

- Password based authentication disabled
- SSH key based authentication
- Secure Kubernetes
    - kube-apiserver
    - Who can access the cluster and what can they do?
    - Who can access:
        - Static token file, Certificates, External Auth Providers - LDAP, Service Accounts
    - What can they do:
        - RBAC authorization, ABAC authorization, Node Authorization, Webhook Mode
- Network Policies

## Authentication

- Different users accessing the cluster: Admins, Developers, End Users, Bots
- There are multiple auth options in the kube-apiserver
- Consider volume mount while providing the auth file in a kubeadm setup

## TLS Certificates

- CA certificates, Root Certificates, Server Certificates
- server certs: apiserver.crt, apiserver.key
- client certs: admin.crt, admin.key, scheduler.crt, scheduler.key, controller-manager.crt, controller-manager.key, kube-proxy.crt, kube-proxy.key, etc
- Only kube apiserver talks to etcd

## Generate Certificates

- Common tools: EASYRSA, OPENSSL, CFSSL
- admin.key: `openssl genrsa -out admin.key 2048`
- admin.csr: `openssl req -new -key admin.key -subj "\CN=kube-admin" -out admin.csr`
- admin.crt : `openssl x509 -in admin.csr -CA ca.crt -CAkey ca.key -out admin.crt`

