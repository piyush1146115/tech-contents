# Fundamentals of NGINX

## What is NGINX

- Nginx is a web server
    - Serves web content
    - Listens on HTTP endpoint and understand HTTP protocol
- Reverse proxy
    - Load Balancing
    - Backend Routing
    - Caching
    - API Gateway

## NGINX Layer4 and Layer7 Proxying

In Layer 4 we see TCP/IP stack only, nothing about the app. We have access to:
- Source IP, source port
- Destination IP, destination port
- Simple packet inspection

In Layer 7 we see the application, HTTP/gRPC etc..
- We have access to more context
- I know where the client is going, which page they are visiting
- Require decryption

- Nginx can operate in layer4 and layer7
- Layer4 proxying is helpful when NGINX doesn't understand the protocol (MySQL database protocol)
- Layer7 proxying is useful when NGINX want to share backend connections and cache results
- Using `stream` context it becomes a layer 4 proxy
- Using `http` context it becomes a layer 7 proxy