# Services and Networking

## Network Policies

Docs: https://kubernetes.io/docs/concepts/services-networking/network-policies/ 

- PolicyTypes: Ingres/egress
- Selector: PodSelector / NamespaceSelector/ ipBlock

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
    name: db-policy
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
   - Ingress
  ingress:
  - from:
    -  podSelector:
         matchLabels:
           name: api-pod
       namespaceSelector:
         matchLabels:
           kubernetes.io/metadata.name: prod
    - ipBlock:
        cidr: 192.168.5.10/32

```

```
kubectl describe netpol payroll-policy
```

## Ingress

Think of Ingress as a Layer 7 loadbalancer built-in on Kubernetes. 

- Ingress controller
- Nginx controller is deployed as just another component in Kubernetes
- Components of Nginx Ingress controller
    - Deployment with deployment config for nginx operator
    - Service
    - ConfigMap with nginx configuration
    - ServiceAccount for auth
- Ingress resource rules

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-wear-watch
spec:
  rules:
  - http:
      paths:
      - path: /wear
        backend:
          service:
            name: wear-service
            port: 80
      - path: /watch
        backend:
          service:
            name: watch-service
            port: 80
```

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-wear-watch
spec:
  rules:
  - host: wear.my-online-store.com
    http:
      paths: /wear
      backend:
        service:
          name: wear-service
          port: 80
  - host: watch.my-online-store.com
    http:
      paths:
      - path: /watch
        backend:
          service:
            name: wear-service
            port: 80            
```
