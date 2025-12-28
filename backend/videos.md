# Videos about backend or DB

- [What are Reactive Databases and why DiceDB exists?](https://youtu.be/V6hi86woFl8?si=y-79sgNNGt-GW-bJ)
- [How do indexes make databases read faster?](https://youtu.be/3G293is403I?si=tAdIDU1WNuTwn961)
- [What are L4 Load Balancers](https://youtu.be/RcarDmgWezY?si=MPM2jnHCxwTKQgq5)
    - L4 load-balacer works in 2 modes- passthrough mode and proxy mode
    - Selection is based on connection-level metadata
    - Source IP and Port, Destination IP and Port Protocol, or some metadata
    - Proxy mode:
        -  LB Terminates client connection
        - Starts a new TCP connection to the backend
        - Two TCP connection exists: Client <> LB <> Backend
        - Example: HAProxy, Envoy, Nginx Stream falls under this category 

- [How PayPal Beat the Thundering Herd Problem and Fixed Their Architecture](https://www.youtube.com/watch?v=pFBCgFzS2W8)
    - A simple solution could be exponential backoff
    - DLQ- unprocessed message gets dumped there
    - Job retry storms can bring down distributed systems
    - Processor service gets overwhelmed when bursts of jobs retry at once
    - Jitter introduces random variation to retry delays to desynchronize retry attempts
        - breaks retry convergence
        - scatters retry attempts across a time window
        - reduces peak loads during degradation
        
- [The Best Programmer I Know • Daniel Terhorst-North • GOTO 2024](https://youtu.be/ybA0zxwgpxw?si=-4zez1i90sksDRFz)
- []()