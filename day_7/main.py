# DAY 7: FUNCTIONS & RECURSION

# 1. Basic function
def greet(name):
    return f"Hello, {name}"

print(greet("Samarth"))


# 2. Function with multiple parameters
def add(a, b):
    return a + b

print("Sum:", add(10, 20))


# 3. Default arguments
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(5, 3))


# 4. *args (multiple positional arguments)
def total_sum(*numbers):
    return sum(numbers)

print("Total:", total_sum(1, 2, 3, 4, 5))


# 5. **kwargs (keyword arguments)
def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(name="Samarth", branch="CSE", year=4)


# 6. Recursion example – factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))
