# ============================================================
# Commit: Day 10 – Implemented lambda functions and functional
# programming tools (map, filter, reduce), including practical
# real-world examples and clean usage patterns.
# ============================================================

from functools import reduce


# 1️⃣ Lambda Function (Anonymous Function)
square = lambda x: x * x
print("Square of 5:", square(5))


# 2️⃣ Lambda with Multiple Arguments
add = lambda a, b: a + b
print("Addition using lambda:", add(10, 20))


# 3️⃣ map() – Apply function to each element
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
print("Squares using map:", squares)


# 4️⃣ map() with Normal Function
def cube(n):
    return n ** 3

cubes = list(map(cube, numbers))
print("Cubes using map:", cubes)


# 5️⃣ filter() – Filter elements based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# 6️⃣ filter() – Prime Numbers from a List
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers:", prime_numbers)


# 7️⃣ reduce() – Reduce list to a single value
sum_of_numbers = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", sum_of_numbers)


# 8️⃣ reduce() – Find Maximum Element
max_number = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum number:", max_number)


# 9️⃣ Chaining map + filter
# Square only even numbers
even_squares = list(
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers))
)
print("Squares of even numbers:", even_squares)


# 🔟 Real-World Example: Student Marks Processing
marks = [35, 67, 89, 23, 90, 56, 40]

# Filter passed students (>=40)
passed = list(filter(lambda x: x >= 40, marks))

# Add grace marks (+5)
grace_marks = list(map(lambda x: x + 5, passed))

# Total marks after grace
total_marks = reduce(lambda a, b: a + b, grace_marks)

print("Passed marks:", passed)
print("Grace marks:", grace_marks)
print("Total marks after grace:", total_marks)


# 1️⃣1️⃣ When NOT to use Lambda (Readability matters)
def percentage(marks):
    return (marks / 100) * 100

percentages = list(map(percentage, grace_marks))
print("Percentages:", percentages)
