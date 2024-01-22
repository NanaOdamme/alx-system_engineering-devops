
## 0x0C. Web server

## What is the main role of a web server?

A web server is a software and/or hardware component that serves as the backbone of the World Wide Web. Its primary role is to handle incoming requests from clients (typically web browsers) and respond by serving web pages, files, or other resources. The web server communicates with clients using the Hypertext Transfer Protocol (HTTP) or its secure variant, HTTPS. The main functions of a web server include processing requests, managing resources, and ensuring the efficient delivery of web content.

## What is a child process?

A child process, in the context of web servers, refers to a spawned or forked instance of the server to handle a specific task or request. Web servers often use a parent-child process model for concurrency. The parent process manages and monitors child processes, while each child process independently handles an incoming request. This approach helps achieve better scalability, resource isolation, and efficient handling of multiple requests.

## Why web servers usually have a parent process and child processes?

Web servers employ a parent-child process model for several reasons:

- **Concurrency:** Child processes allow the web server to handle multiple requests concurrently, improving responsiveness and performance.

- **Scalability:** The ability to dynamically adjust the number of child processes allows the server to scale and accommodate varying levels of traffic.

- **Resource Isolation:** Each child process operates independently, preventing issues with one request from affecting others and enhancing system stability.

- **Efficient Resource Management:** Child processes facilitate the effective use of system resources, and they can be terminated or recycled after handling a specific request.

## What are the main HTTP requests?

HTTP (Hypertext Transfer Protocol) defines several request methods that clients use to communicate with web servers. The main HTTP requests include:

- **GET:** Requests data from a specified resource.
  
- **POST:** Submits data to be processed to a specified resource.

- **PUT:** Updates a resource or creates a new resource if it does not exist.

- **DELETE:** Requests the removal of a specified resource.

- **HEAD:** Requests the headers of a specified resource without the actual data.

- **OPTIONS:** Describes the communication options for the target resource.

These requests form the foundation of client-server communication on the web, enabling various interactions and actions between users and web servers.

