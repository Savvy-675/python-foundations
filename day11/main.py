"""
===========================
Day 11: File & Exception Handling 
Author: Samarth
===========================
"""

# --------------------------------------------------
# Commit: Initialize Day 11 – File and Exception Handling
# --------------------------------------------------

print("=== Day 11: File & Exception Handling ===")


# --------------------------------------------------
# Commit: Basic file writing
# --------------------------------------------------

def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("Data written successfully.")


write_to_file("day11.txt", "Hello Samarth!\nWelcome to Day 11 of Python.")


# --------------------------------------------------
# Commit: File reading using with statement
# --------------------------------------------------

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"


print(read_file("day11.txt"))


# --------------------------------------------------
# Commit: Appending data to file
# --------------------------------------------------

def append_to_file(filename, content):
    with open(filename, "a") as file:
        file.write("\n" + content)
    print("Data appended.")


append_to_file("day11.txt", "Learning Exception Handling now.")


# --------------------------------------------------
# Commit: Handling multiple exceptions
# --------------------------------------------------

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Invalid data type!"
    finally:
        print("Division attempted.")


print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))


# --------------------------------------------------
# Commit: Raising custom exceptions
# --------------------------------------------------

class AgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above.")
    return "Eligible"


try:
    print(check_age(20))
    print(check_age(16))
except AgeError as e:
    print("Custom Exception:", e)


# --------------------------------------------------
# Commit: Logging errors to a file
# --------------------------------------------------

def safe_division(a, b):
    try:
        return a / b
    except Exception as e:
        with open("error_log.txt", "a") as log:
            log.write(str(e) + "\n")
        return "Error logged!"


print(safe_division(5, 0))


# --------------------------------------------------
# Commit: Using built-in module (math)
# --------------------------------------------------

import math

print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))


# --------------------------------------------------
# Commit: Mini real-world example – Student data storage
# --------------------------------------------------

def save_student(name, marks):
    with open("students.txt", "a") as file:
        file.write(f"{name},{marks}\n")


def read_students():
    try:
        with open("students.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


save_student("Samarth", 92)
save_student("Aman", 85)

print("Student Records:")
for student in read_students():
    print(student.strip())

