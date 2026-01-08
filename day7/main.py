# ===============================
# Day 7 - Python All in One
# Focus: Automation & Security Tools
# ===============================

import socket
import os
import time
import re
from datetime import datetime


# ---------- TOOL 1: MULTI-PORT SCANNER ----------
def port_scanner(host, ports):
    print(f"\n[+] Scanning {host}")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((host, port))
            print(f"[OPEN] Port {port}")
            s.close()
        except:
            print(f"[CLOSED] Port {port}")


# ---------- TOOL 2: LOG FILE ANALYZER ----------
def analyze_logs(log_file):
    if not os.path.exists(log_file):
        print("Log file not found")
        return

    error_count = 0
    warning_count = 0

    with open(log_file, "r") as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1

    print("\n[+] Log Analysis Result")
    print("Errors:", error_count)
    print("Warnings:", warning_count)


# ---------- TOOL 3: PASSWORD CHECKER (SAFE DEMO) ----------
def password_wordlist_checker(password, wordlist):
    print("\n[+] Checking password against wordlist")
    for word in wordlist:
        if password == word:
            print("[!] Password found in wordlist (WEAK)")
            return
    print("[✓] Password not found in wordlist")


# ---------- TOOL 4: FILE BACKUP AUTOMATION ----------
def backup_files(source_dir, backup_dir):
    if not os.path.exists(source_dir):
        print("Source directory not found")
        return

    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)

    for file in os.listdir(source_dir):
        src = os.path.join(source_dir, file)
        dst = os.path.join(backup_dir, file)

        if os.path.isfile(src):
            with open(src, "rb") as f_src:
                with open(dst, "wb") as f_dst:
                    f_dst.write(f_src.read())

    print(f"[+] Backup completed from {source_dir} to {backup_dir}")


# ---------- TOOL 5: SIMPLE ACTIVITY LOGGER ----------
def activity_logger(activity):
    with open("activity.log", "a") as f:
        f.write(f"{datetime.now()} - {activity}\n")


# ---------- MAIN EXECUTION ----------
if __name__ == "__main__":

    # Port Scanner
    common_ports = [21, 22, 23, 80, 443]
    port_scanner("google.com", common_ports)
    activity_logger("Port scan completed")

    # Log Analyzer (example file)
    analyze_logs("day5_logs.log")
    activity_logger("Log analysis completed")

    # Password Check
    weak_words = ["password", "123456", "admin", "samarth"]
    password_wordlist_checker("Samarth@123", weak_words)
    activity_logger("Password strength checked")

    # Backup Automation
    backup_files(".", "backup")
    activity_logger("File backup completed")

    print("\nDay 7 Python Completed ✅")
