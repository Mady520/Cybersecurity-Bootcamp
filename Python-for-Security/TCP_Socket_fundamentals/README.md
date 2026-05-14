# TCP Socket Fundamentals

## Objective
A foundational Python project to explore low-level network communications, port binding, and TCP streams. Understanding these mechanics is critical for analyzing network traffic and developing custom security tools.

## Current Capabilities
*   Establishes a reliable TCP connection between a server and client over a specified port.
*   Handles continuous data transmission and graceful connection closure.
*   Built entirely using Python's native `socket` library.

## How to Run
1. Start the server listening on the designated port:
   `python server.py`
2. In a separate terminal, execute the client to connect and send data:
   `python client.py`

## Roadmap & Future Advancements
- [ ] Implement multi-threading to handle concurrent client connections.
- [ ] Upgrade the architecture to function as a basic reverse shell (executing remote system commands).
- [ ] Wrap the data stream in TLS/SSL to prevent plaintext packet sniffing