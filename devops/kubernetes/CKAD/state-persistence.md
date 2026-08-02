# State Persistence

## Intro to Docker Storage

- File System
    - /var/lib/docker
        - aufs
        - containers
        - image
        - volumes
        - data_volume
- Docker builds it's images in layered architecture
- Docker image layer is readonly
- When you run an image using `docker run my-custom-app` a writable container layer gets created on top of read-only layer
- Docker follows copy-on-write mechanism
- To create a new volume: `docker volume create data_volume`
- To mount the created volume: `docker run -v data_volume2:/var/lib/mysql mysql`
- New Command: `docker run --mount type=bind,source=/data/mysql,target=/var/lib/mysql mysql`
- Who is responsible for doing these operation- Storage Drivers
- Example of storage drivers: AUFS, ZFS, BTRFS, Device Mapper, Overlay, Overlay2
- The storage driver option depends on the underline OS


## Volumes in Kubernetes

- hostpath option for a single-node

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: random-number-generator
spec:
  containers:
  - image: alpine
    name: alpine
    command: []
    args:
    volumeMounts:
    - mountPath: /opt
      name: data-volume
  volumes:
  - name: data-volume
    hostPath:
     path: /data
     type: Directory
```

## Persistent Volumes in Kubernetes

- A persistent volume is a cluster-wide pool of storage volume configured by administrator
- AccessModes:
    - ReadOnlyMany
    - ReadWriteMany
    - ReadWriteOnce

```yaml
apiversion: v1
kind: PersistentVolume
metadata:
    name: pv-1

```

## Persistent Volume Claim

- Every Persistent Volume Claim is bound to a single persistent volume

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: myclaim
```

## Storage Classes

- With StorageClasses, you can define a provisioner that can automatically provision storage on a cloud and attach that to Pod when claim is made
-  StorageClass creates PV automatically
- 