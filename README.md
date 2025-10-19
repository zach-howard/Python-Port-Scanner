# Simple TCP Connect Port Scanner

A foundational Python utility designed for efficient network reconnaissance and basic service identification.

---

## Project Overview

This project is a command-line utility that performs a **TCP Connect Scan** on a target IP address. It is a demonstration of core networking principles and efficient socket programming techniques in Python.

- **Objective:** Scan the well-known port range (1 through 1024) to accurately determine which services are actively listening (**OPEN**) on the target host.  
- **Context:** This tool mirrors the initial reconnaissance phase in penetration testing.

---

## Technical Implementation & Demonstrated Skills

This utility showcases specific technical decisions vital for building reliable networking tools:

| Skill Focus        | Implementation Detail         | Value & Rationale |
|--------------------|-------------------------------|-------------------|
| Efficient Scanning | Utilizes `socket.connect_ex()`| Returns an error code instantly (e.g., `0` for success or `10061` for connection refused) instead of raising an exception — faster and more resource-friendly when scanning many ports. |
| Reliability        | Implements `socket.settimeout()` | Prevents the program from freezing indefinitely when connecting to FILTERED ports (silently dropped by a firewall), ensuring the scanner completes. |
| Networking         | TCP Connect method            | Demonstrates understanding of the TCP three-way handshake and how a successful connection attempt identifies an open port. |
| Python Fundamentals| Clear function structure, input validation, and file handling | Displays clean, modular, maintainable Python code suitable for extension and testing. |

---

## How to Run

### 1. Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/zach-howard/Python-Port-Scanner
cd Python-Port-Scanner
```

### 2. Execution

Run the script from your terminal:

```bash
python port_scanner.py
```

### 3. Example Output

The script will prompt you for a target IP address:

```text
Enter the IP address to scan (e.g., 127.0.0.1): 192.168.1.1
---------------------------------------------
Starting scan on target: 192.168.1.1 (Ports 1-1024)
---------------------------------------------
[!] Port 22 is OPEN
[!] Port 80 is OPEN
Scan completed in 1.25 seconds.
```

## Future Enhancements (Showcasing Next Steps)

To transition this basic utility into a professional-grade tool, the following enhancements could be implemented:

- **Multithreading / AsyncIO:** Implement concurrent port checks to reduce scan time from minutes to seconds.
- **Command Line Arguments:** Use the `argparse` module to accept the target IP and custom port ranges directly as command-line arguments (e.g., `python scanner.py -t 10.0.0.1 -p 1-65535`).
- **Service Banner Grabbing:** After identifying an open port, attempt to pull the service banner to identify the running application (e.g., `"Apache 2.4.41"`).
- **Output Formats:** Support JSON / CSV / plain text output for integration with other tools and reporting.
- **Rate Limiting & Polite Defaults:** Prevent accidental DoS and reduce detection by using conservative defaults and optional rate limits.
- **Logging & Tests:** Add structured logging and unit tests for reliability and maintainability.
- **Service Name Lookup:** Use `socket.getservbyport()` (with safe `try/except`) to map well-known ports to service names.
- **CI / Badges:** Add GitHub Actions for tests and linting; add README badges for build status and coverage.

---

## Author

**Zach Howard** - IT Operations Engineer | Cybersecurity Enthusiast

*For collaboration opportunities, feedback, or questions, please open an issue or reach out directly.*

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
