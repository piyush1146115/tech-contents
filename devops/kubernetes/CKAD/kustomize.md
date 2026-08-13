# Kustomize

## Why Kustomize

- We want a way to re-use our Kubernetes configs and only modify what needs to be changed per environment basis
- Kustomize has two config layers: base and Overlays
- Kustomize (Base + Overlays) = Final manifest
- Kustomize comes built-in with kubectl so no other packages need to be installed

## Kustomize vs Helm

- Helm makes use of go templates to allow assigning variables to properties
- Helm is more than just a tool to customize configurations on a per environment basis. Helm is also a package manager for your App
- Helm provides extra features like conditionals, loops, functions and hooks

## kustomization.yaml file

- list of all kubernetes resources required to be managed by Kustomize
- customization that need to be applied

- The kustomize build command combines all the manifests and applies the defined transformations
- The Kustomize build command does not apply/deploy the Kubernetes resources to a cluster
    - The output needs to redirected to the kubectl apply command


```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

# kubernetes resources to be managed by kustomize
resources:
  - nginx-deployment.yaml
  - nginx-service.yaml

# Customizations that need to be made
commonLabels:
    company: KodeKloud
```

## Kustomize output

- `kustomize build k8s/ | kubectl apply -f -`
- `kubectl apply -k k8s/`
- `kustomize build k8s/ | kubectl delete -f -`
- `kubectl delete -k k8s/`

## Managing directories


```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

# sub-dirs containing kustomization.yaml files
resources:
  - api/
  - db/
  - cache/
  - kafka/
  
# Customizations that need to be made
commonLabels:
    company: KodeKloud
```