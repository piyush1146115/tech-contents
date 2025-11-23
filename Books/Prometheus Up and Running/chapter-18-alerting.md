# Alerting

Prometheus is where your logic to determine what is or isn’t alerting is defined. Once an alert is firing in Prometheus, it is sent to an Alertmanager, which can take in alerts from many Prometheus servers. The Alertmanager then groups alerts together and sends you throttled notifications. 

## Alerting Rules

```yaml
groups:
- name: node_rules
rules:
- record: job:up:avg
expr: avg without(instance)(up{job="node"})
- alert: ManyInstancesDown
expr: job:up:avg{job="node"} < 0.5
```

This defines an alert with the name ManyInstancesDown that will fire if more than half of your Node exporters are down. You can tell that it is an alerting rule because it has an alert field rather than a record field.

An alert is identified across evaluation cycles by its labels and does not include the metric name label __name__, but which does include an alertname label with the name of the alert.


### for

Metric-based monitoring involves many race conditions- a scrape may timeout due to a lost network packet, a rule evaluation could be a little delayed due to process scheduling, and the systems you are monitoring could have a brief blip.

```yaml
groups:
- name: node_rules
rules:
- record: job:up:avg
expr: avg without(instance)(up{job="node"})
- alert: ManyInstancesDown
expr: avg without(instance)(up{job="node"}) < 0.5
for: 5m
```

The for field says that a given alert must be returned for at least this long before it starts firing. Until the for condition is met, an alert is considered to be pending. An alert in the pending state but that has not yet fired is not sent to the Alertmanager.

Prometheus has no notion of hysteresis or flapping detection for alerting. You should choose your alert thresholds so that the problem is sufficiently bad that it is worth calling in a human, even if the problem subsequently subsides.

## Alert Labels

When routing alerts in the Alertmanager, you do not want to have to mention the name of every single alert you have individually in ther Alertmanager's configuration file. Instead, you should take advantage of labels to indicate intent.

It is usual for you to have a severity label indicating whether an alert is intended to page someone, and potentially wake them up, or that it is a ticket that can be handled less urgently.

For example, a single machine being down should not be an emergency, but half your machines going down requires urgent investigation:

```yaml
- alert: InstanceDown
expr: up{job="node"} == 0
for: 1h
labels:
severity: ticket
- alert: ManyInstancesDown
expr: job:up:avg{job="node"} < 0.5
for: 5m
labels:
severity: page
```

Prometheus does not permit an alert to have multiple thresholds, but you can define multiple alerts with different thresholds and labels:

```yaml
- alert: FDsNearLimit
expr: >
process_open_fds > process_max_fds * .95
for: 5m
labels:
severity: page
- alert: FDsNearLimit
expr: >
process_open_fds > process_max_fds * .8
for: 5m
labels:
severity: ticket
```