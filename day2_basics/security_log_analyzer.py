# ---------- CONSTANTS (TUPLE) ----------
BLOCK_THRESHOLD = 3
ALLOWED_ROLES = ("admin", "user")

# ---------- USER DATABASE (DICTIONARY) ----------
user = {
    "username": "samarth",
    "role": "admin",
    "active": True
}

# ---------- LOGIN ATTEMPTS (LIST) ----------
login_attempts = [200, 403, 401, 403, 403, 200]

failed_attempts = 0
attempt_number = 0

print("🔐 Security Log Analysis Started\n")

# ---------- ACCESS CHECK (IF + LOGICAL OPS) ----------
if user["active"] and user["role"] in ALLOWED_ROLES:
    print("User access granted\n")
else:
    print("Access denied")
    exit()

# ---------- FOR LOOP (SCAN ATTEMPTS) ----------
for code in login_attempts:
    attempt_number += 1

    # ---------- CONTINUE ----------
    if code == 200:
        print(f"Attempt {attempt_number}: Login successful")
        continue

    # ---------- FAILED LOGIN ----------
    if code == 401 or code == 403:
        failed_attempts += 1
        print(f"Attempt {attempt_number}: Failed login ({code})")

    # ---------- BREAK ----------
    if failed_attempts >= BLOCK_THRESHOLD:
        print("\n🚨 ALERT: User blocked due to multiple failed attempts")
        break

# ---------- WHILE LOOP (POST-BLOCK CHECK) ----------
cooldown = 3
while failed_attempts >= BLOCK_THRESHOLD and cooldown > 0:
    print(f"Cooldown in progress... {cooldown}")
    cooldown -= 1

print("\n📊 Summary")
print("User:", user["username"])
print("Role:", user["role"])
print("Failed Attempts:", failed_attempts)
print("System Status: SAFE" if failed_attempts < BLOCK_THRESHOLD else "System Status: BLOCKED")
