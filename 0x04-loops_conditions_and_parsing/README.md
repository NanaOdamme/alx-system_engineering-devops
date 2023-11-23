```markdown
# Bash Scripting Basics

## Generating SSH Keys
To create SSH keys, use the following command, replacing `my_ssh_key` with your desired key name:
```bash
ssh-keygen -t rsa -b 2048 -f ~/.ssh/my_ssh_key
```

## Shebang: `#!/usr/bin/env bash` vs `#!/bin/bash`
- `#!/usr/bin/env bash` is more flexible and portable as it uses the `env` command to locate the `bash` interpreter in the user's `PATH`.

## Loops
### While Loop
```bash
while [ condition ]; do
  # commands
done
```

### Until Loop
```bash
until [ condition ]; do
  # commands
done
```

### For Loop
```bash
for variable in [list]; do
  # commands
done
```

## Conditional Statements
### If-Else Statement
```bash
if [ condition ]; then
  # commands
else
  # commands
fi
```

### Elif Statement
```bash
if [ condition ]; then
  # commands
elif [ condition ]; then
  # commands
else
  # commands
fi
```

### Case Statement
```bash
case $variable in
  pattern1)
    # commands
    ;;
  pattern2)
    # commands
    ;;
  *)
    # default case
    ;;
esac
```

## Cut Command
The `cut` command is used to extract sections from each line of a file. Example:
```bash
cut -d',' -f1,3 filename.csv
```

## File and Comparison Operators
### File Operators
- `-e filename`: True if the file exists.
- `-f filename`: True if the file exists and is a regular file.
- `-d filename`: True if the file exists and is a directory.

### Comparison Operators
- `-eq`: Equal
- `-ne`: Not equal
- `-lt`: Less than
- `-le`: Less than or equal
- `-gt`: Greater than
- `-ge`: Greater than or equal

Example of using comparison operators in an if statement:
```bash
if [ "$a" -eq "$b" ]; then
  # commands
fi
```
