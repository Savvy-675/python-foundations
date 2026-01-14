# ============================================================
# Commit: Day 9 – Implemented core Python functions, parameters,
# return values, default arguments, nested functions, and
# practical utility examples (even/odd, prime, factorial,
# string reverse, vowel count).
# ============================================================


# 1️⃣ Basic Function
def greet():
    print("Hello, Samarth")


# 2️⃣ Function with Parameters
def greet_person(name):
    print("Hello", name)


# 3️⃣ Function with Return Value
def add(a, b):
    return a + b


# 4️⃣ Default Parameters
def welcome(name="User"):
    return f"Welcome, {name}"


# 5️⃣ Multiple Return Values
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication


# 6️⃣ Nested Function
def outer_function():
    def inner_function():
        return "Inside inner function"
    return inner_function()


# 7️⃣ Even or Odd Check
def is_even(n):
    return n % 2 == 0


# 8️⃣ Prime Number Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 9️⃣ Factorial Function
def factorial(n):
    if n < 0:
        return "Invalid input"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 🔟 Reverse a String
def reverse_string(s):
    return s[::-1]


# 1️⃣1️⃣ Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# ================== FUNCTION CALLS (TESTING) ==================

greet()
greet_person("Samarth")

print("Addition:", add(10, 5))
print(welcome())
print(welcome("Samarth"))

add_res, sub_res, mul_res = calculate(20, 10)
print("Add:", add_res, "Sub:", sub_res, "Mul:", mul_res)

print(outer_function())

print("Is 10 even?", is_even(10))
print("Is 17 prime?", is_prime(17))

print("Factorial of 5:", factorial(5))
print("Reverse of 'Python':", reverse_string("Python"))
print("Vowels in 'Samarth':", count_vowels("Samarth"))
