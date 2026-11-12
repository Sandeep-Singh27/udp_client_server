# UDP Client-Server Communication Using Python Sockets

A simple client-server messaging application built using Python's socket programming interface. The project demonstrates connectionless communication and message exchange using the User Datagram Protocol (UDP).

## Overview

The repository implements two independent components:

- **UDP Server:** Binds to a configured IP address and port, listens for incoming UDP datagrams, displays received messages along with the sender's address, and sends a response back to the originating client.
- **UDP Client:** Sends user-provided messages to the configured server and waits for responses.

The communication uses UDP datagrams through Python's `socket` module. Unlike TCP, UDP does not establish a connection or guarantee message delivery, ordering, or retransmission.

The server can receive datagrams from different clients without maintaining individual client connections.

## Architecture

```text
              UDP CLIENT                         UDP SERVER
           ┌──────────────────┐              ┌──────────────────┐
           │                  │              │                  │
           │  Create Socket   │              │  Create Socket   │
           │        │         │              │        │         │
           │  Read Message    │              │  Bind IP & Port  │
           │        │         │              │        │         │
           │  Send Datagram   ├─────────────►│  Receive Datagram│
           │                  │              │        │         │
           │                  │              │  Extract Sender  │
           │                  │              │     Address      │
           │                  │              │        │         │
           │                  │              │  Process Message │
           │                  │              │        │         │
           │  Receive Reply   │◄─────────────┤  Send Response   │
           │        │         │              │                  │
           │  Display Reply   │              │  Wait for Next   │
           │                  │              │    Datagram      │
           └──────────────────┘              └──────────────────┘
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| Socket | UDP network communication |
| python-dotenv | Environment variable management |
| os | Accessing environment configuration |

## Project Structure

```text
udp_client_server/
│
├── udp_client.py    # UDP client for sending messages and receiving responses
├── udp_server.py    # UDP server for receiving messages and sending responses
├── sample.env       # Sample server IP address and port configuration
├── .gitignore       # Git exclusion rules
└── README.md        # Project documentation
```
