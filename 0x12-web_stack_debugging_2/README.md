# Project: Web Stack Debugging 2

## 0. I Am Someone Else
This script, `0-iamsomeoneelse`, is a Bash script that accepts one argument and runs the `whoami` command under the user passed as an argument. This script allows you to switch to a different user temporarily.

### Example Usage:
```bash
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```

### Repo Details:
- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- **Directory:** `0x12-web_stack_debugging_2`
- **File:** `0-iamsomeoneelse`

## 1. Run Nginx as Nginx
In the `1-run_nginx_as_nginx` script, we address the security concern of running Nginx as the root user. The script configures the container to ensure Nginx is running as the less privileged `nginx` user, listening on all active IPs on port 8080.

### Requirements:
- Nginx must be running as `nginx` user.
- Nginx must be listening on all active IPs on port 8080.
- Cannot use `apt-get remove`.
- Bash script to configure the container to meet the requirements.

### After Debugging:
```bash
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

### Repo Details:
- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- **Directory:** `0x12-web_stack_debugging_2`
- **File:** `1-run_nginx_as_nginx`

## 2. 7 Lines or Less
The `100-fix_in_7_lines_or_less` script is an advanced version of the previous task. It is concise, meeting the same requirements with a Bash script of 7 lines or less.

### Requirements:
- Bash script must be 7 lines long or less.
- There must be a new line at the end of the file.
- Respect Bash script requirements.
- Cannot use `;`, `&&`, `wget`, or execute the previous answer file.

### Repo Details:
- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- **Directory:** `0x12-web_stack_debugging_2`
- **File:** `100-fix_in_7_lines_or_less`
