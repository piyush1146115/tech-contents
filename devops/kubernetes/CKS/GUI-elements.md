# K8s GUI elements

## Refs
- https://github.com/kubernetes/dashboard
- dashbord-args: https://github.com/kubernetes/dashboard/blob/master/docs/common/arguments.md


## Kubectl proxy
- Creates a proxy server between localhost and the Kubernetes API server
- Uses connection as configured in the kubeconfig
- Allows to access API locally just over http and without authentication
- We can also use port-forward to access a port

## Install dashboard

```
root@cks-master:~# helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
"kubernetes-dashboard" has been added to your repositories
root@cks-master:~# helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
Release "kubernetes-dashboard" does not exist. Installing it now.
NAME: kubernetes-dashboard
LAST DEPLOYED: Fri Jun 27 21:50:15 2025
NAMESPACE: kubernetes-dashboard
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
*************************************************************************************************
*** PLEASE BE PATIENT: Kubernetes Dashboard may need a few minutes to get up and become ready ***
*************************************************************************************************

Congratulations! You have just installed Kubernetes Dashboard in your cluster.

To access Dashboard run:
  kubectl -n kubernetes-dashboard port-forward svc/kubernetes-dashboard-kong-proxy 8443:443

NOTE: In case port-forward command does not work, make sure that kong service name is correct.
      Check the services in Kubernetes Dashboard namespace using:
        kubectl -n kubernetes-dashboard get svc

Dashboard will be available at:
  https://localhost:8443
root@cks-master:~#
```


```
root@cks-master:~# k get pods,svc -n kubernetes-dashboard
NAME                                                       READY   STATUS    RESTARTS   AGE
pod/kubernetes-dashboard-api-7c89f58cc7-g5pp4              1/1     Running   0          106s
pod/kubernetes-dashboard-auth-54b69c68f9-ldhsz             1/1     Running   0          106s
pod/kubernetes-dashboard-kong-79867c9c48-nkl7r             1/1     Running   0          106s
pod/kubernetes-dashboard-metrics-scraper-547874fcf-82lfg   1/1     Running   0          106s
pod/kubernetes-dashboard-web-7796b9fbbb-6sh74              1/1     Running   0          106s

NAME                                           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/kubernetes-dashboard-api               ClusterIP   10.97.166.123    <none>        8000/TCP   107s
service/kubernetes-dashboard-auth              ClusterIP   10.107.110.58    <none>        8000/TCP   107s
service/kubernetes-dashboard-kong-proxy        ClusterIP   10.106.190.248   <none>        443/TCP    107s
service/kubernetes-dashboard-metrics-scraper   ClusterIP   10.103.99.9      <none>        8000/TCP   107s
service/kubernetes-dashboard-web               ClusterIP   10.103.198.15    <none>        8000/TCP   107s
```

