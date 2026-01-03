# Chapter 01: Reliable, Scalable, and Maintainable Applications

A data-intensive application is typically built from standard building blocks that provide commonly needed functionality. For example, many application need to:
- Store data so that they, or another application can find it again later (databases)
- Remember the result of an expensive operation, to speed up reads (caches)
- Allow users to search data by keyword or filter it in various ways (search indexes)
- Send a message to another process, to be handled asynchrounously (stream processing)
- Periodically crunch a large amount of accumulated data (batch processing)


When you combine several tools in order to provide a service, the service’s interface
or application programming interface (API) usually hides those implementation
details from clients.

In this book, we focus on three concerns that are important in most software systems:
- Reliability: The system should continue to work correctly even in the face of adversity
- Scalability: As the system grows, there should be reasonable ways of dealing with that growth
- Maintainability: Over time, many different people will work on the system and they should all be able to work on it productively

## Reliability

We can understand reliability as meaning, roughly, “continuing to work correctly, even when things go wrong.”

The things that can go wrong are called faults, and systems that anticipate faults and can cope with them are called fault-tolerant or resilient. 

Note that a fault is not the same as a failure. A fault is usually defined as one component of the system deviating from its spec, whereas a failure is when the system as a whole stops providing the required service to the user. It is impossible to reduce the probability of a fault to zero; therefore it is usually best to design fault-tolerance mechanisms that prevent faults from causing failures.

- **Hardware faults**: Hard disks crash, RAM becomes faulty, the power grid has a blackout, someone
unplugs the wrong network cable. Anyone who has worked with large datacenters
can tell you that these things happen all the time when you have a lot of machines.

- **Software Errors**: Another class of fault is a systematic error within the system. Such faults are
harder to anticipate, and because they are correlated across nodes, they tend to cause many more system failures than uncorrelated hardware faults.  The bugs that cause these kinds of software faults often lie dormant for a long time until they are triggered by an unusual set of circumstances. In those circumstances, it is revealed that the software is making some kind of assumption about its environ‐
ment—and while that assumption is usually true, it eventually stops being true for some reason.

- **Human Errors**: Humans design and build software systems, and the operators who keep the systems
running are also human. Even when they have the best intentions, humans are known to be unreliable. For example, one study of large internet services found that configuration errors by operators were the leading cause of outages, whereas hardware faults (servers or network) played a role in only 10–25% of outages.

## Scalability

Even if a system is working reliably today, that doesn’t mean it will necessarily work
reliably in the future. Scalability is the term we use to describe a system’s ability to cope with increased load. Note, however, that it is not a one-dimensional label that we can attach to a system: it is meaningless to say “X is scalable” or “Y doesn’t scale.” Rather, discussing scalability means considering questions like “If the system grows in a particular way, what are our options for coping with the growth?” and “How can we add computing resources to handle the additional load?”


**Latency and response time**: Latency and response time are often used synonymously, but they
are not the same. The response time is what the client sees: besides the actual time to process the request (the service time), it includes network delays and queueing delays. Latency is the duration that a request is waiting to be handled—during which it is latent, awaiting service. 

## Describing Performance

Once you have described the load on your system, you can investigate what happens
when the load increases. You can look at it in two ways:
- When you increase a load parameter and keep the system resources (CPU, memory, network bandwidth, etc.) unchanged, how is the performance of your system
affected?
- When you increase a load parameter, how much do you need to increase the resources if you want to keep performance unchanged?

Usually it is better to use percentiles. If you take your list of response times and sort it from fastest to slowest, then the median is the halfway point. For example, if your median response time is 200 ms, that means half your requests return in less than 200 ms, and half your requests take longer than that.

In order to figure out how bad your outliers are, you can look at higher percentiles: the 95th, 99th, and 99.9th percentiles are common (abbreviated p95, p99, and p999). They are the response time thresholds at which 95%, 99%, or 99.9% of requests are
faster than that particular threshold. For example, if the 95th percentile response time is 1.5 seconds, that means 95 out of 100 requests take less than 1.5 seconds, and 5 outof 100 requests take 1.5 seconds or more.

Percentiles are often used in service level objectives (SLOs) and service level agreements (SLAs), contracts that define the expected performance and availability of a service. An SLA may state that the service is considered to be up if it has a median response time of less than 200 ms and a 99th percentile under 1 s (if the response time is longer, it might as well be down), and the service may be required to be up at least 99.9% of the time. 

## Approaches for Coping with Load

An architecture that is appropriate for one level of load is unlikely to cope with 10 times that load. If you are working on a fast-growing service, it is therefore likely that you will need to rethink your architecture on every order of magnitude load increase
—or perhaps even more often than that.

Some systems are elastic, meaning that they can automatically add computing resources when they detect a load increase, whereas other systems are scaled manually (a human analyzes the capacity and decides to add more machines to the system). An
elastic system can be useful if load is highly unpredictable, but manually scaled systems are simpler and may have fewer operational surprises.

An architecture that scales well for a particular application is built around assumptions of which operations will be common and which will be rare—the load parameters. If those assumptions turn out to be wrong, the engineering effort for scaling is at
best wasted, and at worst counterproductive. In an early-stage startup or an unproven product it’s usually more important to be able to iterate quickly on product features than it is to scale to some hypothetical future load.

## Maintainability

It is well known that the majority of the cost of software is not in its initial development, but in its ongoing maintenance—fixing bugs, keeping its systems operational, investigating failures, adapting it to new platforms, modifying it for new use cases,
repaying technical debt, and adding new features.

However, we can and should design software in such a way that it will hopefully minimize pain during maintenance, and thus avoid creating legacy software ourselves. To this end, we will pay particular attention to three design principles for software
systems:
- **Operability**: Make it easy for operations teams to keep the system running smoothly.
- **Simplicity**: Make it easy for new engineers to understand the system, by removing as much
complexity as possible from the system.
- **Evolvability**: Make it easy for engineers to make changes to the system in the future, adapting
it for unanticipated use cases as requirements change. Also known as extensibility, modifiability, or plasticity.

### Simplicity: Managing Complexity

Small software projects can have delightfully simple and expressive code, but as projects get larger, they often become very complex and difficult to understand. 

There are various possible symptoms of complexity: explosion of the state space, tight coupling of modules, tangled dependencies, inconsistent naming and terminology, hacks aimed at solving performance problems, special-casing to work around issues
elsewhere, and many more.

When complexity makes maintenance hard, budgets and schedules are often overrun. In complex software, there is also a greater risk of introducing bugs when making a change: when the system is harder for developers to understand and reason about, hidden assumptions, unintended consequences, and unexpected interactions are more easily overlooked. Making a system simpler does not necessarily mean reducing its functionality; it can also mean removing accidental complexity.

One of the best tools we have for removing accidental complexity is abstraction. A good abstraction can hide a great deal of implementation detail behind a clean, simple-to-understand façade. A good abstraction can also be used for a wide range of
different applications.

For example, high-level programming languages are abstractions that hide machine code, CPU registers, and syscalls. SQL is an abstraction that hides complex on-disk and in-memory data structures, concurrent requests from other clients, and inconsis‐
tencies after crashes.

### Evolvability: Making Change Easy

It’s extremely unlikely that your system’s requirements will remain unchanged for‐
ever. They are much more likely to be in constant flux: you learn new facts, previously unanticipated use cases emerge, business priorities change, users request new features, new platforms replace old platforms, legal or regulatory requirements
change, growth of the system forces architectural changes, etc.

Most discussions of these Agile techniques focus on a fairly small, local scale (a couple of source code files within the same application). In this book, we search for ways of increasing agility on the level of a larger data system, perhaps consisting of several
different applications or services with different characteristics.

There is unfortunately no easy fix for making applications reliable, scalable, or maintainable. However, there are certain patterns and techniques that keep reappearing in different kinds of applications. In the next few chapters we will take a look at some examples of data systems and analyze how they work toward those goals.