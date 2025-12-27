# Videos related to Distributed Systems


## Martin Kleppman Playlist

Playlist link: https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB

### Lecture 1: Introduction

Link: https://www.youtube.com/watch?v=UEAMfLPZZhE&list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB&index=1 

Leslie Lamport definition of Distributed System: A system in which the failure of a computer didn't even know existed can render your own computed unusable.


In general a distrbuted system consists of multiple computeres communicating via a network and trying to achieve some task together. Consists of "nodes" (Computer, phone, car, robot).

**Why make a system distributed?**
- It's inherently distributed: sending a message from your mobile phone to your friend's phone
- For better reliability: even if one node fails, the system as a whole keeps functioning
- For better performance: get data from a nearby node rather than one halfway round the world
- To solve bigger problems: huge amounts of data, can't fit on one machine

**Why not make a system distributed**
- Communication may fail 
- Processes may crash
- All of this may happen nondeterministacally

**Fault Tolerance**: We want the system as a whole to continue working, even some parts are faulty. This is hard.

### Lecture 2: Distributed Systems and Computer Networking

Link: https://youtu.be/1F3DEq8ML1U?si=4AQXngNIQa74-POi

Fundamental abstraction of a distributed systems; One node can send a message to another node.

- Latency and Bandwidth: 
    - Latency: Time until message arrives
    - Bandwidth: Data volume per unit time
- Web demo of a website of data flowing through

