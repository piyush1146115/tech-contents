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