# Configurations

## ENV Variables in K8s

```yaml
env:
    - name: APP_COLOR
      value: pink

```


```yaml
env:
    - name: APP_COLOR
      valueFrom:
        configMapKeyRef:
```

## ConfigMaps

- Create ConfigMap
- Inject the config into Pod

```bash
$ kubectl create configmap <config-name> --from-literal=<key>=<value>
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: blue
  APP_MODE: prod
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
    ports:
      - containerPort: 8080
    envFrom:
      - configMapRef:
          name: app-config
```

```yaml
- env:
  - name: APP_COLOR
    valueFrom:
      configMapKeyRef:
        name: webapp-config-map
        key: APP_COLOR
```

## Secrets

```bash
> kubectl create secret generic <secret-name> --from-literal=<key>=<value>
```


## Resource requirements

```yaml
resources:
  requests:
  limits:
```

- LimitRange is applicable for Namespace level
- ResourceQuota is applicable at Namespace level

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: my-resource-quota
spec:
  hard: requests.cpu
  requests.memory: 4Gi
  limits.cpu: 10
  limits.memory: 10Gi
```

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: cpu-resource-constraint
spec:
  limits:
  - default:
      cpu: 500m
    defaultRequest:
      cpu: 500m
    max:
      cpu: "1"
    min:
      cpu: 100m
    type: Container
```

## Taints and Toleration

- Taints are set on Node
- Tolerations are set on Pod

- Taint effects:
    - NoSchedule
    - PreferNoSchedule
    - NoExecute

```bash
> kubectl taint nodes node-name key=value:taint-effect
```

```bash
> kubectl taint nodes node1 app=myapp:NoSchedule
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  spec:
    containers:
    - name: nginx-container
      image: nginx
    tolerations:
      - key: "app"
        operator: "Equal"
        value: "myapp"
        effect: "NoSchedule"
```