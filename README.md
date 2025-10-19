# Simple TCP Port Scanner (Python)

## ⚙️ Project Description
This is a basic network reconnaissance utility built in Python. It demonstrates foundational skills in **network security** and **socket programming**. The tool scans a specified target IP address across the well-known port range (1-1024) to identify listening services.

## ✨ Demonstrated Skills
* **Python Programming:** File I/O, functions, and control flow.
* **Networking Fundamentals:** Understanding of **TCP/IP** and **Port Services**.
* **Socket Programming (`socket` library):** Implementation of the `connect_ex()` method for efficient connection attempts.
* **Error Handling:** Using `settimeout()` to prevent the scanner from hanging on closed ports.

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/RepoName.git](https://github.com/YourUsername/RepoName.git)
    cd RepoName
    ```
2.  **Run the script:**
    ```bash
    python port_scanner.py
    ```
3.  Enter the target IP address when prompted (e.g., `127.0.0.1` for local testing).