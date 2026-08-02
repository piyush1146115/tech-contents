# Security

## Custom Resource Definition

- fligtTicket custom resource

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
    name: flighttickets.flights.com
specs:
    scope: Namespaced
    group: flights.com
    names:
        kind: FlightTicket
        singular: flightticket
        plural: flighttickets
        shortnames:
          - ft
    versions:
      - name: v1
        served: true
        storage: true
```

## Custom Controller

- To control the lifecycle of CRDs

## Operator Framework

- One of the good operator is etcd operator
- CRD: EtcdCluster, EtcdBackup, EtcdRestore
- Custom Controller: ETCD Controller, Backup Operator, Restore Operator
- Operator hub: Operator.ai
