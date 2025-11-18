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

