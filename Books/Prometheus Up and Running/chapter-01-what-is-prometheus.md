# What is Prometheus

Prometheus is an open source, metrics-based monitoring system. Prometheus does one thing and it does it well. It has a simple yet powerful data model and a query language that lets you analyse how your applications and infrastructure are performing.

## What is monitoring

In the context of computer systems, we can narrow down the operational monitoring  down to these four things:
- Alerting
- Debugging
- Trending
- Plumbing

## Categories in Monitoring

At the end of the day, most monitoring is about the same thing: events. Events can be almost anything, including:
- Receiving a HTTP request
- Sending a HTTP 400 response
- Entering a function
- Reaching the else of an if statement
- Leaving a function

**Profiling**: Profiling takes the approach that you can't have all the context for all of the events all the time, but you can have some of the conext for limited periods of time.

**Tracing**: Tracing doesn't look at all events, rather it takes some proportion of events such as one in a hundred that pass through some functions of interest. From this you can get an idea of where your program is spending time and which code paths are most contributing to latency.

**Logging**: Logging looks at a limited set of events and records some of the context for each of these events. For example, it may look at all incoming HTTP requests, or all outgoing database calls. Different types of logging have different uses, durability, and retention requirements. As I see it, there are four general an somewhat overlapping categories:
- Transaction logs
- Request logs
- Application logs
- Debug logs


**Metrics**: Metrics largely ingore context, instead tracking aggregations over time of different types of events. To keep resource usage sane, the amount of different numbers being tracked needs to be limited.

Metrics allow you to collect information about events from all over your process, but with generally no more than one or two fields of context with bounded cardinality. Logs allow you to collect information about all of one type of event, but can only track a hundred fields of context with unbounded cardinality.

As a metrics-based monitoring system, Prometheus is designed to track overall system health, behaviour, and performance rather than individual events. Put another way, Prometheus cares that there were 15 requests in the last minute that took 4 seconds to handle, resulted in 40 database calls, 17 cache hits and 2 purchases by customers. The cost and code paths of the individual calls would be the concern of profiling and logging.


## Prometheus Architecture

### Client Libraries

Metrics do not magically spring forth from applications; someone has to add the instrumentation that produces them. This is where client libraries come in. Client libraries are available for all the major languages and runtimes.

Client libraries take care of all the nitty-gritty details such as thread-safety, bookkeeping, and producing the Prometheus text exposition format in response to HTTP requests.

### Exporters

Not all code you run is code that you can control or even have access to, and thus adding direct instrumentation isn't really an option.

An exporter is a piece of software that you deploy right beside the application you want to obtain metrics from. It takes in requests from Prometheus, gathers the required data from the application, transforms them into the correct format, and finally returns them in a response to Prometheus. You can think of an exporter as a small one-to-one proxy, converting data between the metrics interface of an application and the Prometheus exposition format.

### Service Discovery

Once you have all your applications instrumented and your exporters running, Prometheus needs to know where they are. This is so Prometheus will know what is meant to monitor and be able to notice if something it is meant to be monitoring is not responding.

### Scraping

Prometheus does this by sending a HTTP request called scrape. The response to the scrape is parsed and ingested into storage. Scrapes happen regularly; usually you would configure it to happen every 10 to 60 seconds for each target.

Prometheus is a pull-based system. It decides when and what to scrape, based on its configuration. There are also push-based systems, where the monitoring target decides if it is going to be monitored and how often.

### Storage

Prometheus stores data locally in a custom database. Distributed systems are challenging to make reliable, so Prometheus does not attempt to do any form of clustering. In addition to reliability, this makes Prometheus easier to run.

### Dashboards

Prometheus has a number of HTTP APIs that allow you to both request raw data and evaluate PromQL queries. These can be used to produce graphs and dashboards. Out of the box, Prometheus provides the expression browser. It uses these APIs and is suitable for ad hoc querying and data exploration. It is recommended to use Grafana for dashboards.

### Alert Management

The Alertmanager receives alerts from Prometheus servers and turns them into notifications. Notifications can include email, chat applcations such as Slack, and services such as PagerDuty.

The Alertmanager does more than blindly turn alerts into notifications on a one-to-one basis. Related alerts can be aggregated into one notification, throttled to reduce pager storms, and different routing and notificaiton outputs can be configured for each of your different teams. Alerts can also be silenced, perhaps to snooze an issue you are already aware of in advance when you know maintenance is scheduled.


### Long term storage

Since Prometheus stores data only on the local machine, you are limited by how much disk space you can fit on that machine. While you usually care only about the most recent day or so worth of data, for long-term capacity planning a longer retention period is desirable.

Prometheus does not offer a clustered storage solution to store data acros multiple machines, but there are remote read and write APIs that allow other systems to hook in and take on this role. These allow PromQL queries to be transparently run against both local and remote data.


## What Prometheus Is Not

It is not a best choice for high cardinality data, such as email address or usernames.

Promtheus is designed for operational monitoring, where small inaccuracies and race conditions due to factors like kernal scheduling and failed scrapes are a fact of life. Prometheus makes tradeoffs and prefers giving you data that is 99.99% correct over your monitoring breaking while waiting for perfect data.
