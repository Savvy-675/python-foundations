# DAY 8: DATA STRUCTURES

# 1. Lists
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
print("List:", numbers)
print("Sliced List:", numbers[1:4])


# 2. Tuples (immutable)
coordinates = (10, 20)
print("Tuple:", coordinates)


# 3. Sets (unique values)
unique_numbers = {1, 2, 3, 3, 4, 5}
unique_numbers.add(6)
print("Set:", unique_numbers)


# 4. Dictionary
student = {
    "name": "Samarth",
    "branch": "CSE",
    "year": 4
}

student["college"] = "Engineering College"
print("Dictionary:", student)


# 5. Looping through dictionary
for key, value in student.items():
    print(key, "->", value)


# 6. Practical example – frequency counter
sentence = "python makes you think better"
freq = {}

for char in sentence:
    if char != " ":
        freq[char] = freq.get(char, 0) + 1

print("Character Frequency:", freq)
