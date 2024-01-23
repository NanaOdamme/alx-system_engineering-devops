Certainly! Below is a template for a README file for your debugging project. You can customize it based on your specific details.

---

# Debugging Project: Apache2 Container Configuration

## Overview

This project involves debugging an issue with an Apache2 container where it fails to return the expected page containing "Hello Holberton" when querying the root of the container. The initial issue is observed as an empty reply or an error message when using `curl`. The goal is to access the container, identify and fix the configuration issues, and ensure that Apache2 serves the expected content.

## Instructions

### Prerequisites

- [Docker](https://www.docker.com/) installed on the host machine.

### Steps to Reproduce the Issue

1. Run the Docker container:

   ```bash
   docker run -p 8080:80 -d -it holbertonschool/265-0
   ```

2. Check the container's status:

   ```bash
   docker ps
   ```

3. Use `curl` to query the root of the container:

   ```bash
   curl 0:8080
   ```

   Observe the error message or empty reply.

### Debugging Steps

1. Access the running container:

   ```bash
   docker exec -it <container_id> /bin/bash
   ```

   Replace `<container_id>` with the actual container ID.

2. Navigate to the Apache configuration directory:

   ```bash
   cd /etc/apache2/sites-available/
   ```

3. Edit the default virtual host configuration using a text editor:

   ```bash
   vi 000-default.conf
   ```

   Update the `DocumentRoot` directive to point to the correct directory.

4. Create an HTML file with the desired content:

   ```bash
   echo "Hello Holberton" > /var/www/html/index.html
   ```

5. Restart Apache:

   ```bash
   service apache2 restart
   ```

   or

   ```bash
   systemctl restart apache2
   ```

6. Exit the container:

   ```bash
   exit
   ```

7. Re-run `curl` from the host machine:

   ```bash
   curl 0:8080
   ```

   Confirm that it returns the expected content.

## Files

- **Dockerfile**: The Dockerfile used to build the container image.
- **README.md**: This README file providing instructions and information about the debugging project.

## Author

Your Name

## Acknowledgments

# 0x0D. Web stack debugging #0
# Debugging Project: Apache2 Container Configuration

## Overview

This project involves debugging an issue with an Apache2 container where it fails to return the expected page containing "Hello Holberton" when querying the root of the container. The initial issue is observed as an empty reply or an error message when using `curl`. The goal is to access the container, identify and fix the configuration issues, and ensure that Apache2 serves the expected content.

## Instructions

### Prerequisites

- [Docker](https://www.docker.com/) installed on the host machine.

### Steps to Reproduce the Issue

1. Run the Docker container:

   ```bash
   docker run -p 8080:80 -d -it holbertonschool/265-0
   ```

2. Check the container's status:

   ```bash
   docker ps
   ```

3. Use `curl` to query the root of the container:

   ```bash
   curl 0:8080
   ```

   Observe the error message or empty reply.

### Debugging Steps

1. Access the running container:

   ```bash
   docker exec -it <container_id> /bin/bash
   ```

   Replace `<container_id>` with the actual container ID.

2. Navigate to the Apache configuration directory:

   ```bash
   cd /etc/apache2/sites-available/
   ```

3. Edit the default virtual host configuration using a text editor:

   ```bash
   vi 000-default.conf
   ```

   Update the `DocumentRoot` directive to point to the correct directory.

4. Create an HTML file with the desired content:

   ```bash
   echo "Hello Holberton" > /var/www/html/index.html
   ```

5. start Apache:

   ```bash
   service apache2 start

6. Exit the container:

   ```bash
   exit
   ```

7. Re-run `curl` from the host machine:

   ```bash
   curl 0:8080
   ```

   Confirm that it returns the expected content.

## Authors

Nana Akosua
