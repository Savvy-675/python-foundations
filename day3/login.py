# Simple Security Access Monitor (Day 3 – All Concepts)

# predefined credentials
CORRECT_USER = "admin"
CORRECT_PASS = "root123"

# open ports in system 
open_ports = [22, 80, 443]

attempts = 0
max_attempts = 3
authenticated = False

# ---------------- LOGIN SYSTEM ----------------
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == CORRECT_USER and password == CORRECT_PASS:
        print("\nLogin successful ")
        authenticated = True
        break
    else:
        attempts += 1
        print(f"Login failed  | Attempts left: {max_attempts - attempts}")

if not authenticated:
    print("\nAccount locked due to multiple failed attempts ")
else:
    # ---------------- ACCESS LEVEL CHECK ----------------
    ip = input("\nEnter your IP address: ")

    if ip.startswith("192.168"):
        print("Internal network access granted ")
    else:
        print("External network access detected ")

    # ---------------- PORT SCANNING ----------------
    print("\nScanning ports 20 to 30...\n")

    for port in range(20, 31):

        if port == 25:
            continue  # skip mail port intentionally

        if port in open_ports:
            print(f"Port {port} → OPEN")
        else:
            print(f"Port {port} → CLOSED")

        if port == 30:
            print("\nScan completed ✔️")
            break

    # ---------------- SUSPICIOUS ACTIVITY CHECK ----------------
    failed_logins = attempts

    if failed_logins == 0:
        print("\nStatus: Normal activity 🟢")
    elif failed_logins <= 2:
        print("\nStatus: Mildly suspicious 🟡")
    else:
        print("\nStatus: High risk 🔴")

print("\nProgram terminated.")
