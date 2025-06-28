# NetworkPolicy

- It's possible to have mutiple NetworkPolicy selecting for same pod
- If a pod has more than one networkpolicy then the union of all the applied networkpolicy is applied; order doesn't matter

## Refs:
- https://kubernetes.io/docs/concepts/services-networking/network-policies/#default-deny-all-egress-traffic
- https://github.com/killer-sh/cks-course-environment/tree/master/course-content/cluster-setup/network-policies



## Hands on lab on netowork policy

Create backend and frontend pods:

```
root@cks-master:~# k run frontend --image=nginx
pod/frontend created
root@cks-master:~# k run backend --image=nginx
pod/backend created
root@cks-master:~# k expose pod frontend --port 80
service/frontend exposed
root@cks-master:~# k expose pod backend --port 80
service/backend exposed
root@cks-master:~# k get pod
NAME       READY   STATUS    RESTARTS   AGE
backend    1/1     Running   0          57s
frontend   1/1     Running   0          75s
root@cks-master:~# k get pod, svc
error: arguments in resource/name form must have a single resource and name
root@cks-master:~# k get pod,svc
NAME           READY   STATUS    RESTARTS   AGE
pod/backend    1/1     Running   0          71s
pod/frontend   1/1     Running   0          89s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/backend      ClusterIP   10.103.34.111   <none>        80/TCP    21s
service/frontend     ClusterIP   10.110.96.77    <none>        80/TCP    33s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   13d
```

Check connectivity:

```
root@cks-master:~# k exec frontend -- curl backend
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   615  100   615    0     0    989      0 --:--:-- --:--:-- --:--:--   988
<!DOCTYPE html>
```

Apply the default deny network policy:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-egress
spec:
  podSelector: {}
  policyTypes:
  - Egress

```

After applying default deny NP, try to reach from one pod to another:
```yaml
root@cks-master:~# k exec frontend -- curl backend
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:15 --:--:--     0

rl: (6) Could not resolve host: backend
command terminated with exit code 6
```

A second policy to allow egress from frontend pod:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: frontend-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      run: frontend
  policyTypes:
  - Egress
  egress:
  - to:
    - podSelector:
        matchLabels:
          run: backend
```

policy to allow ingress in backend pod:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      run: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          run: frontend
```

Allow DNS resolution

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: dns-policy
  namespace: default
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
  egress:
      ports:
        - port: 53
          protocol: UDP
        - port: 53
          protocol: TCP
```

Create a ns cassandra
```
k create ns cassandra
```

Add a label in the cassandra ns:
```
$ k edit ns cassandra
ns: cassandra
```

Create a pod in Cassandra namespace:
```
k -n cassandra run cassandra --image=nginx
```

Try to reach the cassandra pod from the backend pod, it should be blocked:
```
root@cks-master:~# k exec backend -- curl 192.168.1.4
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:06 --:--:--     0
```

Update the backend networkpolicy to support egress to Cassandra:

root@cks-master:~# k edit networkpolicy backend-network-policy
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-network-policy-cassandra
  namespace: default
spec:
  podSelector:
    matchLabels:
      run: backend
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          run: frontend
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          ns: cassandra
```


Try again to reach the cassandra pod:
```
root@cks-master:~# k exec backend -- curl 192.168.1.4
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   615  100   615    0     0   390k      0 --:--:-- --:--:-- --:--:--  600k
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```