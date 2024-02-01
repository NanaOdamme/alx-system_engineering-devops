# HTTPS and SSL/TLS

## HTTPS
HTTPS, or HyperText Transfer Protocol Secure, is the secure version of HTTP, the protocol used for transmitting data between a user's web browser and a website. It adds a layer of security by encrypting the data during transmission, making it more difficult for unauthorized parties to intercept and access sensitive information.

## SSL/TLS
SSL (Secure Sockets Layer) and its successor, TLS (Transport Layer Security), are cryptographic protocols that provide secure communication over a computer network. SSL is an older version, while TLS is the more modern and widely adopted one. These protocols ensure the confidentiality and integrity of data exchanged between a user and a website.

## Two Main Elements SSL Provides
1. **Encryption:** SSL/TLS encrypts the data exchanged between the user's browser and the website, preventing unauthorized parties from deciphering the information.
2. **Authentication:** SSL/TLS authenticates the identity of the website, ensuring that users are connecting to the intended server and not a malicious one.

## HAProxy SSL Termination on Ubuntu 16.04
HAProxy is a widely-used load balancer, and SSL termination refers to the practice of offloading SSL/TLS processing from the web servers to the load balancer. This can enhance performance and simplify certificate management. Refer to the documentation for setting up SSL termination with HAProxy on Ubuntu 16.04.

## Bash Functions
### awk
`awk` is a powerful programming language for pattern scanning and processing. The `man awk` command in the terminal provides the manual for awk, offering detailed information on its usage and functionalities.

### dig
`dig` is a command-line tool for querying DNS (Domain Name System) servers. Running `man dig` in the terminal provides the manual for dig, explaining its various options and how to use them.

## HTTPS SSL 2 Main Roles
1. **Data Encryption:** HTTPS ensures that data exchanged between the user and the website is encrypted, making it unreadable to unauthorized entities.
2. **Authentication:** SSL certificates validate the identity of the website, assuring users that they are connecting to a legitimate and trusted server.

## Purpose of Encrypting Traffic
Encrypting traffic is crucial for protecting sensitive information (such as login credentials, personal details, and financial transactions) from eavesdroppers and hackers. It prevents unauthorized access to data during transmission.

## SSL Termination
SSL termination is the process of decrypting SSL-encrypted traffic at a load balancer or reverse proxy before forwarding it to the web servers. This allows the load balancer to handle SSL/TLS negotiations, reducing the computational load on the backend servers.
