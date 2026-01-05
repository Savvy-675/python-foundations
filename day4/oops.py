def greet(name, age=18):
    return f"Hello {name}, Age: {age}"

print(greet("Samarth", 21))


# ---------- *args and **kwargs ----------
def add_numbers(*args):
    return sum(args)

def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(add_numbers(1, 2, 3, 4))
user_profile(name="Samarth", role="CSE Student", interest="Cybersecurity")


# ---------- LAMBDA FUNCTIONS ----------
square = lambda x: x * x
print("Square:", square(5))


# ---------- COMPREHENSIONS ----------
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [n for n in numbers if n % 2 == 0]
square_dict = {n: n*n for n in numbers}
unique_set = {n for n in numbers if n > 3}

print(even_numbers)
print(square_dict)
print(unique_set)


# ---------- EXCEPTION HANDLING ----------
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution completed")


# ---------- FILE HANDLING ----------
file_name = "day4_demo.txt"

# Write to file
with open(file_name, "w") as f:
    f.write("Day 4 Python File Handling\n")
    f.write("Learning Python seriously.\n")

# Read from file
with open(file_name, "r") as f:
    content = f.read()
    print(content)


# ---------- MODULE CHECK ----------
def main():
    print("This file is running directly")

if __name__ == "__main__":
    main()


# ---------- OOP BASICS ----------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"


class Student(Person):
    def __init__(self, name, age, branch):
        super().__init__(name, age)
        self.branch = branch

    def details(self):
        return f"{self.name}, {self.age}, Branch: {self.branch}"


s1 = Student("Samarth", 21, "CSE")
print(s1.introduce())
print(s1.details())


# ---------- MINI UTILITY ----------
def password_strength(password):
    if len(password) < 8:
        return "Weak password"
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return "Strong password"
    return "Moderate password"

print(password_strength("Samarth123"))


# ---------- END ----------
print("Day 4 Python Completed ✅")
