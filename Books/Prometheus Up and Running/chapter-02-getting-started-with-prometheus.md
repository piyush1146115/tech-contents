# Getting Started with Prometheus

Download and install Prometheus: https://prometheus.io/download/

```yaml
# my global config
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9090"]
       # The label name is added as a label `label_name=<label_value>` to any timeseries scraped from this config.
        labels:
          app: "prometheus"

```

### Using the Expression Browser

The expression browser is useful for running ad hoc queries, developing PromQL expressions, and debugging both PromQL and the data inside Prometheus.

To start, make sure you are in the Console view, enter the expression up, and click Execute.
The job label here comes from the job_name in the prometheus.yml. Prometheus does not magically know that it is scraping a Prometheus and thus that it should use a job label with the value prometheus.

Next, you should evaluate process_resident_memory_bytes or process_virtual_memory_max_bytes. The convention in Prometheus is to use
base units such as bytes and seconds, and leave pretty printing it to frontend tools
like Grafana. Metrics like process_resident_memory_bytes are called **gauges**. For a gauge, it is its
current absolute value that is important to you. There is a second core type of metric
called the counter. **Counters** track how many events have happened, or the total size
of all the events. Let’s look at a counter by graphing prometheus_tsdb_head_
samples_appended_total, the number of samples Prometheus has ingested. Counters are always increasing. This creates nice up and to the right graphs, but the values of counters are not much use on their own. What you really want to know is how fast the counter is increasing, which is where the rate function comes in. The
rate function calculates how fast a counter is increasing per second. Adjust your expression to rate(prometheus_tsdb_head_samples_appended_total[1m]), which will calculate how many samples Prometheus is ingesting per second averaged over one minute and produce a result.

### Running the Node Exporter

The Node exporter exposes kernel and machine-level metrics on Unix systems, such as Linux. It provides all the standard metrics such as CPU, memory, disk space, disk I/O, and network bandwidth. 

## Alerting

There are two parts to alerting. First, adding alerting rules to Prometheus, defining the logic of what constitutes an alert. Second, the Alertmanager converts firing alerts into notifications, such as emails, pages, and chat messages. For alerting rules you need a PromQL expression that returns only the results that you wish to alert on. 