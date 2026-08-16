# Imperative commands

```bash
> kubectl run --help
> kubectl run redis --image=redis:alipine --labels="tier=db"
> kubectl expose redis --port 6379 --name redis-service

> kubectl create deployment webapp --image=kodekloud/webapp-color --replicas=3

> kubectl run custom-nginx --image=-nginx --port=8080

> kubectl create ns dev-ns

> kubectl create deployment redis-deploy --image=redis --replicas=2 -n dev-ns

```