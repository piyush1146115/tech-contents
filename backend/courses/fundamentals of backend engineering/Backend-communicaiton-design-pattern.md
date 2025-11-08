# Backend communication design pattern

## Server Sent Events

One request, a very very long response. 

Limitations of Request/response:
- Vanila request/response isn't ideal for notification
- Client wants real time notification from backend
    - A user just logged in
    - A message is just received 
- Push works but restrictive


What is Server Sent Events:
- A response has start and end
- Client sends a request 
- Server sends logical events as part of response
- Server never writes the end of the respense
- It is still a request but and unending response
-  Client parses the stream data looking for the events
- Works with request/response (HTTP)

Pros:
- Real time
- Compatible with Request/response

Cons:
- Clients must be online
- Clients might not be able to handle
- Polling is preferred for light clients
- HTTP/1.1 problem

## Publish Subscribe (Pub/Sub)

One publisher, many readers.

Pros:
- Scales with multiple receivers
- Great for microservices
- Loose coupling
- Works while clients not running

Cons:
- Message delivery issues
- Complexity
- Network saturation

## Multiplexing vs Demultiplexing (h2 proxying vs Connection Pooling)

- Connection Pooling

## Stateful vs Stateless

- Is state stored in the backend
- Stateful:
    - Stores state about clients in its memory
    - Depends on the information being there
    - A protocol can be also stateful or stateless
- Stateless
    - Client is responsible to "transfer the state" with every request
    - May store but can safely lose it
    - Stateless backends can still store data somewhere else
    - Can you restart the backend during idle time while the client workflow continues to work?
- Stateful vs Stateless protocols
    - The procols can be designed to store state
    - TCP is stateful: Sequences, Connection file descriptor
    - UDP is stateless
        - DNS send queryID in UDP to identify queries
        - QUIC sends connectionID to identify connection

    - You can build a stateless protocol on top of a stateful one and vise versa
    - HTTP on top of TCP
        - HTTP is stateless while TCP is stateful
        - If TCP breaks, HTTP blindly create another one
        - QUIC on top of UDP
- Complete stateless system
    - Stateless systems are rare
    - State is carried with every request
    - A backend service that relies completely on the input. Examples:
        - Check if input param is a prime number
        - JWT (JSON Web Token)


## Sidecar Pattern

- Thick clients, thicker backends
- Every protocol requires a library. Like HTTP, HTTPS, TLS, GRPC every protocol requires a library
- Changing the library is hard
    - Once you use the library your app is entrenched
    - App & Library "should" be same language
    - Changing the library require retesting
    - Adding features to the library is hard
- When if we delegate communication?
    - Proxy communicate instead
    - Proxy has the rich library
    - Meet sidecar pattern
- HTTP/1.1 client -> Client sidecar proxy -> HTTP/2+Secure -> Server sidecar reverse proxy -> http/1.1 server

**Sidecar examples:**
- Service mesh proxies
    - Linkerd, Istio, Envoy
- Sidecar Proxy container
- Must be Layer 7 Proxy

**Pros and Cons of Sidecar Proxy**
Pros:
- Language agnostic
- Protocol upgrade
- Security
- Tracing and monitoring
- Service discovery
- Caching

Cons:
- Complexity
- Latency
- 
