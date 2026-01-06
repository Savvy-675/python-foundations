# ===============================
# Day 5 - Python All in One
# Focus: System, Security & Automation
# ===============================

import os
import sys
import re
import hashlib
import subprocess
import logging
from datetime import datetime


# ---------- SYS MODULE ----------
print("Python Version:", sys.version)
print("Command Line Arguments:", sys.argv)


# ---------- OS MODULE ----------
current_dir = os.getcwd()
print("Current Directory:", current_dir)

print("Files in directory:")
for file in os.listdir(current_dir):
    print("-", file)


# ---------- ENVIRONMENT VARIABLES ----------
os.environ["APP_MODE"] = "DEVELOPMENT"
print("App Mode:", os.getenv("APP_MODE"))


# ---------- DATETIME ----------
now = datetime.now()
print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


# ---------- REGEX ----------
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def validate_email(email):
    return bool(re.match(email_pattern, email))

print("Email valid:", validate_email("samarth@gmail.com"))
print("Email valid:", validate_email("samarth@com"))


# ---------- HASHLIB (PASSWORD HASHING) ----------
def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

password = "Samarth@123"
hashed_password = hash_password(password)

print("Original Password:", password)
print("Hashed Password:", hashed_password)


# ---------- FILE LOGGING ----------
logging.basicConfig(
    filename="day5_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Day 5 script started")
logging.warning("This is a warning example")
logging.info("Password hashing completed")


# ---------- SUBPROCESS ----------
try:
    result = subprocess.run(
        ["python", "--version"],
        capture_output=True,
        text=True
    )
    print("Subprocess Output:", result.stdout.strip())
except Exception as e:
    print("Subprocess error:", e)


# ---------- MINI SECURITY UTILITY ----------
def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if re.search(r"[A-Z]", password) and re.search(r"[0-9]", password) and re.search(r"[@$!%*?&]", password):
        return "Strong"
    return "Moderate"

print("Password strength:", check_password_strength("Samarth@123"))


# ---------- AUTOMATION THINKING ----------
def auto_create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created")
    else:
        print(f"Folder '{folder_name}' already exists")

auto_create_folder("reports")


# ---------- END ----------
print("Day 5 Python Completed ✅")
logging.info("Day 5 script finished successfully")
