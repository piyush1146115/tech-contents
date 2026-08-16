# Pod Design

## Rolling Updates and Rollbacks

```bash
> kubectl rollout status deployment/myapp-deploy
```

Rolling strategies:
- Recreate
- RollingUpdate


## Jobs/Cronjobs

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: throw-dice-job
spec:
  template:
    spec:
      containers:
      - name: throw-dice-job
        image: kodekloud/throw-dice
      restartPolicy: Never
  backoffLimit: 35
  completions: 3
  parallelism: 3
```