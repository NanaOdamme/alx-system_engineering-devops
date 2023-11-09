Command line challenge and sftp

---

# SFTP File Transfer

This guide explains how to use the `put` command in SFTP to transfer files from your local machine to a remote terminal.

## Prerequisites

- Access to a terminal or command prompt on your local machine.
- SFTP access to the remote server.

## Steps

1. **Open Terminal:**
   Open your terminal or command prompt on your local machine.

2. **Navigate to the Directory:**
   Use the `cd` command to navigate to the directory where your files are located.

   ```bash
   cd path/to/your/files
   ```

3. **Connect to Remote Server:**
   Start the SFTP session and connect to the remote server. Replace `username` with your actual username and `remote.example.com` with the address of the remote server.

   ```bash
   sftp username@remote.example.com
   ```

   Enter your password when prompted.

4. **Use `put` Command:**
   Once connected, you can use the `put` command to transfer files from your local machine to the remote server.

   ```bash
   put filename
   ```

   Replace `filename` with the actual name of the file you want to transfer.

   If you have multiple files, you can use wildcards to transfer them all.

   ```bash
   put *.txt
   ```

5. **Check Transfer:**
   After transferring files, you can use the `ls` command to check if the files are now on the remote server.

   ```bash
   ls
   ```

6. **Close SFTP Session:**
   When you're done transferring files, you can close the SFTP session.

   ```bash
   exit

