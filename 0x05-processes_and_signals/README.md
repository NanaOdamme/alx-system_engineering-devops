
# Basic Unix Commands for Process Management

## 1. PID (Process ID)
A PID (Process ID) is a unique numerical identifier assigned to each running process in a computer system.

## 2. Process
A process is an instance of a computer program that is being executed by one or many threads. It has its own memory space, system resources, and a unique PID.

## 3. Finding a Process’ PID
Use the `ps` command to list processes and their PIDs:
```bash
ps aux
```
Use `pgrep` to find PIDs based on process names:
```bash
pgrep process_name
```

## 4. Killing a Process
The `kill` command terminates a process by PID:
```bash
kill PID
```
The `pkill` command terminates processes based on their names:
```bash
pkill process_name
```

## 5. Signal
A signal is a software interrupt delivered to a process, used for communication between processes and with the operating system.

## 6. Two Unignorable Signals
- **SIGKILL (9):**
  ```bash
  kill -9 PID
  ```
- **SIGSTOP (19 or 20):**
  ```bash
  kill -STOP PID   # Pauses the process
  kill -CONT PID   # Resumes the process
  ```

**Note:** Use caution when using signals, especially SIGKILL, as it forcefully terminates processes and may lead to undesired consequences.
