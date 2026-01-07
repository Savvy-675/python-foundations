# ===============================
# Day 6 - Python All in One
# Focus: Networking, APIs & Concurrency
# ===============================

import socket
import threading
import requests
import json
import time


# ---------- SOCKET PROGRAMMING ----------
def tcp_client(host="example.com", port=80):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)
        client.connect((host, port))

        request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
        client.send(request.encode())

        response = client.recv(4096)
        print("Socket Response:\n", response.decode(errors="ignore"))

        client.close()
    except Exception as e:
        print("Socket Error:", e)

# Uncomment to test
# tcp_client()


# ---------- REQUESTS (API CALLS) ----------
def fetch_api_data():
    try:
        response = requests.get("https://api.github.com", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("GitHub API keys:", list(data.keys()))
        else:
            print("API Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

fetch_api_data()


# ---------- JSON HANDLING ----------
sample_data = {
    "name": "Samarth",
    "role": "CSE Student",
    "skills": ["Python", "Networking", "Cybersecurity"]
}

json_string = json.dumps(sample_data, indent=4)
print("JSON String:\n", json_string)

parsed_data = json.loads(json_string)
print("Parsed Name:", parsed_data["name"])


# ---------- THREADING ----------
def task(name, delay):
    for i in range(3):
        print(f"{name} running iteration {i}")
        time.sleep(delay)

thread1 = threading.Thread(target=task, args=("Thread-1", 1))
thread2 = threading.Thread(target=task, args=("Thread-2", 1.5))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads completed")


# ---------- MINI PORT CHECKER ----------
def check_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        print(f"Port {port} OPEN on {host}")
        s.close()
    except:
        print(f"Port {port} CLOSED on {host}")

check_port("google.com", 80)
check_port("google.com", 22)


# ---------- BASIC RATE LIMITER ----------
def rate_limited_request(url, delay=2):
    print("Sending request to:", url)
    time.sleep(delay)
    try:
        r = requests.get(url, timeout=5)
        print("Status:", r.status_code)
    except:
        print("Request failed")

rate_limited_request("https://httpbin.org/get")


# ---------- END ----------
print("Day 6 Python Completed ✅")
