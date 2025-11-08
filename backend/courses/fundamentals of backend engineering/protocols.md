# Backend Protocols

## Protocol Properties

- Don't memorize the properties
- Whether the protocol solves your backend design problem or not, that's all matter


### What is a protocol

- A system that allows two parties to communicate
- A protocol is desinged with a set of properties
- Depending on the purpose of the protocol
- TCP, UDP, HTTP, gRPC, FTP


### Protocol Properties

- Data format
    - Text based (plain text, JSON, XML)
    - Binary (protobug, RESP, h2, h3)
- Transfer mode
    - Message based (UDP, HTTP)
    - Stram (TCP, WebRTC)
- Addressing system
    - DNS name, IP, MAC
- Directionality
    - Bidirectional (TCP)
    - Unidirectional (HTTP)
    - Full/Half duplex
- State
    - Stateful (TCP, gRPC, Apache thrift)
    - Stateless (UDP, HTTP)
- Routing:
    - Proxies, Gateways
- Flow and congestion control
    - TCP (Flow and Congestion)
    - UDP (No control)
- Error management:
    - Error code
    - Retries and timeouts


## OSI Model : Open System Interconnection

### Why do we need a communication model
- Agnostic applications
    - Without a standard model, your application must have knowledge of the underlying network medium
    - Imagine you have to author different version of your app so that it works on wifi vs ethernet vs LTE vs fiber
- Network equipment management
    - Without a standard model, upgrading network equipments become difficult
- Decoupled Innovation
    - Innovation can be done in each layer separately without affecting rest of the models

### What is the OSI model?

- 7 layers each describe a specific networking component
- Layer 7: Application- HTTP/gRPC/FTP
- Layer 6: Presentation - Encoding, Serialization
- Layer 5: Session - Connection establishment, TLS
- Layer 4: Transport - UDP/TCP
- Layer 3: Network - IP
- Layer 2: Data link - Frames, Mac address Ethernet
- Layer 1: Physical - Electric signals, fiber or radio wave


**OSI layer example on sender side with a POST request:**
- Layer 7 - Application: POST request with JSON data to HTTPS server
- Layer 6 - Presentation: Serialize JSON to flat byte strings
- Layer 5 - Session: Request to establish TCP connection/TLS
- Layer 4 - Transport: Sends SYN request target port 443
- Layer 3 - Network: SYN is placed an IP packet(S) and adds the source/dest IPs
- Layer 2- Data link: Each packet goes into a single frame and adds the source/dest
- Layer 1- Physical: Each frame becomes string of bits which converted into either radio signal(wifi), electrical signal (ethernet), or light (fiber)

**OSI layer example on receiver side:**
- Layer 1- Physical:
    - Radio, electrical or light is received and converted into digital bits
- Layer 2- Data link:
    - The bits from Layer 1 is assembled into frames
- Layer 3- Network:
    - The frames from layer 2 are assembled into IP packet
- Layer 4- Transport
    - The IP packets from layer 3 are assembled into TCP segments
    - Deals with congestion control/flow control/retransmission in case of TCP
    - If Segment is SYN, we don't need to go further into more layers as we are still processing the connection request
- Layer 5- Session
    - The connection session is established or identified
    - We only arrive at this layer when necessary (3 way handshake is done)
- Layer 6- Presentation
    - Deserialize flat byte strings back to JSON for the app to consume
- Layer 7- Application
    - Application understands the JSON POST request and your express json or apache request receive event is triggered 
- Take it with a grain of salt, it's not always cut and dry

The shortcomings of the OSI model:
- OSI model has too many layers which can be hard to comprehend
- Hard to argue about which layer does what
- Simpler to deal with layers 5-6-7 as just one layer, application. TCP/IP model does just that