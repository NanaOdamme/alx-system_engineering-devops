# System Engineering & DevOps - SSH Configuration

## Overview

This repository documents the steps and configurations performed as part of a System Engineering and DevOps session focused on SSH configuration. The session covered topics such as SSH key management, server configuration, and Puppet automation.

## Tasks Completed

### 1. SSH Key Pair Generation

- Created an SSH key pair using the `ssh-keygen` command.
- Generated a 2048-bit RSA key pair.
- Stored the private key in `~/.ssh/school` and the public key in `~/.ssh/school.pub`.

### 2. SSH Connection to Remote Host

- Established an SSH connection to a remote host using the private key `~/.ssh/school`.
- Connected to the remote host as the user `ubuntu`.

### 3. Puppet Configuration for SSH

- Created a Puppet manifest (`100-puppet_ssh_config.pp`) to automate SSH configurations.
- Used Puppet to manage SSH private key and deny password authentication.
- Applied the Puppet manifest using the `sudo puppet apply` command.

## File Structure

- **README.md:** This documentation file.
- **0-use_a_private_key:** Bash script to connect to a server using an SSH private key.
- **100-puppet_ssh_config.pp:** Puppet manifest for managing SSH configurations.

## Notes

- Warnings about deprecated Ruby methods (`URI.escape`) were observed during Puppet apply, but they are informational and do not impact functionality.
- A notice about the deprecation of `hiera.yaml` version 3 was encountered, suggesting consideration for an upgrade to version 5 in the future.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository/0x0B-ssh
   ```

2. Execute the Bash script to connect to a remote server:

   ```bash
   ./0-use_a_private_key
   ```

3. Apply the Puppet manifest to configure SSH settings:

   ```bash
   sudo puppet apply 100-puppet_ssh_config.pp
   ```.
