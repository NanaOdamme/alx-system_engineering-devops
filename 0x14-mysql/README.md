# MySQL Configuration and Backup

This repository contains scripts and configurations for setting up and managing MySQL on web-01 and web-02 servers.

## Installation

### Task 0: Install MySQL

Make sure MySQL 5.7.x is installed on both web-01 and web-02 servers. Verify the installation using the following command:

```bash
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```

Ensure that SSH configuration from task #3 is completed for both servers.

Repository:
- GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- Directory: 0x14-mysql

### Task 1: Let us in!

Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn. Grant necessary permissions:

```bash
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
```

Ensure SSH project task #3 is completed for both servers.

Repository:
- GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- Directory: 0x14-mysql

### Task 2: If only you could see what I've seen with your eyes

Create a database named tyrell_corp on web-01, and within it, create a table named nexus6 with at least one entry. Make sure holberton_user has SELECT permissions on the table.

```bash
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
```

Repository:
- GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- Directory: 0x14-mysql

### Task 3: Quite an experience to live in fear, isn't it?

Create a new user replica_user on web-01 with host % for the replica server. Ensure holberton_user has SELECT privileges on the mysql.user table.

```bash
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
```

Repository:
- GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- Directory: 0x14-mysql

### Task 4: Setup a Primary-Replica infrastructure using MySQL

Set up replication for the MySQL database named tyrell_corp. Primary must be hosted on web-01, and the replica must be hosted on web-02. Provide configurations for primary and replica.

Repository:
- GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- Directory: 0x14-mysql
- Files: 4-mysql_configuration_primary, 4-mysql_configuration_replica

### Task 5: MySQL backup

Write a Bash script that generates a MySQL dump, creates a compressed archive, and follows the specified naming format. The script accepts one argument, the password used to connect to the MySQL database.

```bash
ubuntu@03-web-01:~$ ls
5-mysql_backup
ubuntu@03-web-01:~$ ./5-mysql_backup mydummypassword
backup.sql
ubuntu@03-web-01:~$ ls
01-03-2017.tar.gz  5-mysql_backup  backup.sql
ubuntu@03-web-01:~$ more backup.sql
-- MySQL dump 10.13  Distrib 5.7.25, for debian-linux-gnu (x86_64)
...
ubuntu@03-web-01:~$ file 01-03-2017.tar.gz
01-03-2017.tar.gz: gzip compressed data, from Unix, last modified: Wed Mar  1 23:38:09 2017
ubuntu@03-web-01:~$
```

Repository:
- GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- Directory: 0x14-mysql
- File: 5-mysql_backup
