# Multi container Pods

- Multi container pods share the same network and file system layer

## Multi container pods design patterns

- Co-located containers (no order of startup)
- Regular init-containers
- Sidecar containers (sidecar container starts first)

- If initContainer has restartPolicy set to Always, it doesn't die in the init step and works like sidecar container

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  initContainers:
    - name: init-myservice
      image: busybox:1.31
      command: ["sh", "-c", "until nslookup myservice; do echo waiting for myservice; sleep 2; done;"]
    - name: init-mydb
      image: busybox:1.31
      command: ["sh", "-c", "until nslookup mydb; do echo waiting for mydb; sleep 2; done;"]
  containers:
    - name: myapp-container
      image: busybox:1.28
      command: ["sh", "-c", "echo The app is running! && sleep 3600"]
```

Starting with Kubernetes v1.33, sidecar containers are natively supported. This allows sidecar containers to follow a defined lifecycle relative to the main containers in the Pod — without requiring entrypoint hacks.

## How Native Sidecars Work

Declared using the `restartPolicy: Always` field inside the initContainers block.

Kubernetes treats such containers as sidecars, ensuring they:
- Start before main containers.
- Run alongside them.
- Shut down after the main containers complete.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sidecar-example
spec:
  initContainers:
    - name: sidecar-logger
      image: busybox:1.31
      restartPolicy: Always
      command: ["sh", "-c", "while true; do echo Sidecar running; sleep 10; done"]
  containers:
    - name: main-app
      image: busybox:1.31
      command: ["sh", "-c", "echo Main app starting; sleep 60"]
```