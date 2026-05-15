# 02: Reconnaissance 

This folder contains scripts focused on network discovery and service enumeration. These are foundational tools built to understand how scanners interact with open and closed ports.

## Scripts in this folder:
* **`simple_port_scanner.py`**: A basic sequential scanner using `socket` and instance timeouts.
* **`cli_port_scanner.py`**: A command-line based scanner demonstrating `sys.argv` and robust error handling (`KeyboardInterrupt`, `socket.error`).
* **`banner_grabber.py`**: A script demonstrating both passive (listening) and active (sending HTTP requests) service identification.

## How to use:
These scripts are designed to be run from the command line.

Example for the CLI scanner:
\`\`\`bash
python3 scanner.py <target_ip> ---> for the cli_port_scanner 
python Simple_port_scanner.py 
python Basic_banner_grabber  
\`\`\`

## Key Learnings:
* How to use `s.connect_ex()` instead of `s.connect()` to avoid crashing on closed ports.
* The difference between passive banner grabbing (SSH) and active banner grabbing (HTTP).
* How to gracefully handle user interrupts (Ctrl+C) during a scan.