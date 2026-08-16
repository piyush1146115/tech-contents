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

## Transformers

- commonLabel - adds a label to all Kubernetes resources
- namePrefix/Suffix- adds a common prefix-suffix to all resource names
- Namespace - adds a common namespace to all resources
- commonAnnotations - adds an annotation to all resources

```yaml
namePrefix: KodeKloud-
nameSuffix: -dev
namespace: lab
commonLabel: dev
commonAnnotations:
  branch: master
```

### Image Transformers

```yaml
images:
  - name: nginx
    newName: haproxy
    newTag: "v1.2.4"
```

## Patches

- Kustomize patches provide another method to modifying Kubernetes configs
- Unlike common transformers, patches provide a more surgical approach to targeting one or more specific sections in a Kubernetes resource
- To create a patch 3 parameters must be provided:
  - Operation Type: add/remove/replace
  - Target: what resource should this patch be applied on
    - Kind
    - Version/Group
    - Name
    - Namespace
    - labelSelector
    - AnnotationSelector
  - Value: What is the value that will either be replaced or added with (only needed for add/replace operations)

There are two kinds of patch:
- Json 6902 Patch
- Strategic Merge Patch

```yaml
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: replace
        path: /spec/replicas
        value: 5
```

```yaml
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: add
        path: /spec/template/metadata/labels/org
        value: KodeKloud
```

```yaml
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: remove
        path: /spec/template/metadata/labels/org
```

## Overlays


- k8s
  - base
    - kustomization.yaml
    - db
      - db-deploy.yaml
      - db-service.yaml
      - kustomization.yaml
    - api
      - api-deploy.yaml
      - api-service.yaml
      - kustomization.yaml
- overlays
  - dev
    - db
      - db-patch.yaml
      - kustomization.yaml
    - api
      - api-patch.yaml
      - kustomization.yaml
  - prod
    - kustomization.yaml
    - db
      - db-patch
      - kustomization.yaml
    - api
      - api-patch.yaml
      - kustomization.yaml
