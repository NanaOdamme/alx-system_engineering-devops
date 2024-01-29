# Web Stack Debugging 1

This repository documents the debugging process for resolving issues related to an Nginx web server configuration. The debugging was performed in the context of the ALX System Engineering & DevOps curriculum.

## Problem Statement

The initial problem was identified as the Nginx web server not properly listening on port 80, resulting in a "503 Service Unavailable" error.

## Debugging Steps

1. **Check Nginx Status:**
   - Run `sudo service nginx status` to verify if Nginx is running.

2. **Identify Configuration Issue:**
   - Examine the Nginx error log with `sudo tail -f /var/log/nginx/error.log` for any syntax errors or configuration issues.

3. **Check Listening Ports:**
   - Confirm that Nginx is listening on port 80 using `netstat -tuln | grep :80`.

4. **Inspect Nginx Configuration:**
   - Review the Nginx configuration files, especially the default configuration at `/etc/nginx/sites-enabled/default`.

5. **Resolve Duplicate Default Server Issue:**
   - Address the "duplicate default server" issue in the configuration file by removing redundant server blocks.

6. **Verify Nginx Configuration:**
   - Test the Nginx configuration with `sudo nginx -t` to ensure there are no syntax errors.

7. **Restart Nginx:**
   - Restart Nginx using `sudo service nginx restart`.

8. **Identify Running Processes:**
   - Use `sudo ss -tuln | grep :80` to identify processes using port 80.

9. **Kill Conflicting Process:**
   - If needed, terminate the process conflicting with port 80 using `sudo kill -9 <PID>`.

10. **Finalize Configuration:**
    - After resolving conflicts, finalize the Nginx configuration and restart the service.

## Scripts Used

### Nginx Configuration Script

```bash
#!/usr/bin/env bash

sudo sed -i "s/8080/80/" /etc/nginx/sites-enabled/default
sudo service nginx restart
