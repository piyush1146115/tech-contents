# Platform Security

## Supply Chain Security - Minimize base image footprint

- Base vs Parent Image
- Build modular images
- Don't persist state inside container

## Scan image

- `trivy image --severity CRITICAL nginx:1.18.0`
-  `trivy image archive-image.tar`

Best practices:
- Continuously rescan images
- Kubernetes Admission Controllers to scan images
- Have your own reository with pre-scanned images ready to go
- Integrate scanning into your CI/CD pipeline

## Image Repository Security

```
kubectl create secret docker-registry regcred \
 --docker-server=private-registry.io \
 --docker-username=registry-user \
 --docker-password=registry-password \
 --docer-email=registry-user@org.com
```

## Observability Overview

- Falco
    - Monitor Syscalls

### Falco Overview

- Policy Engine
- Libraries
- Falco Rules
- Falco Kernal Modules

- Falco rules
    - rule
    -  descritption
    -  condition
    - output
    - priority


## Service Mesh and Istio
