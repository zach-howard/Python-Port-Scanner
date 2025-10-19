import socket

# --- 1. CORE SCANNING FUNCTION ---
def scan_port(target_ip, port):
    # Create a new socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set the timeout to 1 second
    s.settimeout(1)
    
    # Attempt to connect to the target IP and port
    # connect_ex returns 0 if successful, non-zero otherwise
    result = s.connect_ex((target_ip, port))
    
    # Close the socket
    s.close()
    
    return result

# --- 2. MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    # Get target IP from the user
    target = input("Enter the IP address to scan (e.g., 127.0.0.1): ")

    print("-" * 30)
    print(f"Starting scan on target: {target}")
    print("-" * 30)
    
    # Loop through ports 1 to 1024 (the well-known ports)
    for port in range(1, 1025):
        # Call the core function
        response = scan_port(target, port)
        
        # Check if the connection attempt was successful (response == 0)
        if response == 0:
            # Add a clear indicator that the port is OPEN
            print(f"Port {port} is OPEN")