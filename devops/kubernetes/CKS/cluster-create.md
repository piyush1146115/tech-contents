# Cluster Creation

List gcloud projects: ~ $ gcloud projects list
Set the right project: ~ $ gcloud config set project kkkk

Create Worker instance:
```
gcloud compute instances create cks-worker --zone=asia-south1-a \
--machine-type=e2-medium \
--image=ubuntu-2004-focal-v20220419 \
--image-project=ubuntu-os-cloud \
--boot-disk-size=100GB
```

Create Master instance:
```
gcloud compute instances create cks-master --zone=asia-south1-a \
--machine-type=e2-medium \
--image=ubuntu-2004-focal-v20220419 \
--image-project=ubuntu-os-cloud \
--boot-disk-size=200GB
```

## INSTALL cks-master
```
~ [1]$ gcloud compute ssh --zone "asia-south1-a" "cks-master"

sudo -i
bash <(curl -s https://raw.githubusercontent.com/killer-sh/cks-course-environment/master/cluster-setup/latest/install_master.sh)
```
Command to join a node in the cluster will be given at the end of the script like this:
### COMMAND TO ADD A WORKER NODE ###
kubeadm join 10.160.0.3:6443 --token 
kubeadm join 10.160.0.3:6443 --token 0rnpt5.r72vgv31c22eo57g --discovery-token-ca-cert-hash sha256:57c28332e4916e9dc6615bc54698de7a093d09c219033fec7395647074d5349c

## INSTALL cks-worker
```
gcloud compute ssh --zone "asia-south1-a" "cks-worker"

sudo -i

bash <(curl -s https://raw.githubusercontent.com/killer-sh/cks-course-environment/master/cluster-setup/latest/install_worker.sh)
```

EXECUTE ON MASTER: kubeadm token create --print-join-command --ttl 0
THEN RUN THE OUTPUT AS COMMAND HERE TO ADD AS WORKER

## Interacting with the cluster

Run as root in the VM to access the cluster
```
piyush@cks-master:~$ sudo -i
root@cks-master:~# kubectl get nodes
NAME         STATUS   ROLES           AGE     VERSION
cks-master   Ready    control-plane   11m     v1.32.3
cks-worker   Ready    <none>          3m49s   v1.32.3
root@cks-master:~# kubectl get pods -A
NAMESPACE     NAME                                      READY   STATUS    RESTARTS   AGE
kube-system   calico-kube-controllers-fdf5f5495-hdlss   1/1     Running   0          11m
kube-system   canal-4xrqn                               2/2     Running   0          4m17s
kube-system   canal-5hwlb                               2/2     Running   0          11m
kube-system   coredns-668d6bf9bc-mjbzr                  1/1     Running   0          11m
kube-system   coredns-668d6bf9bc-rgt82                  1/1     Running   0          11m
kube-system   etcd-cks-master                           1/1     Running   0          11m
kube-system   kube-apiserver-cks-master                 1/1     Running   0          11m
kube-system   kube-controller-manager-cks-master        1/1     Running   0          11m
kube-system   kube-proxy-g6snr                          1/1     Running   0          4m17s
kube-system   kube-proxy-wcr6t                          1/1     Running   0          11m
kube-system   kube-scheduler-cks-master                 1/1     Running   0          11m
root@cks-master:~#
```