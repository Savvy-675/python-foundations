"""
===========================
Day 12: Object-Oriented Programming (OOP)
Author: Samarth
===========================
"""

# --------------------------------------------------
# Commit: Initialize Day 12 – OOP Concepts
# --------------------------------------------------

print("=== Day 12: Object-Oriented Programming ===")


# --------------------------------------------------
# Commit: Create a basic class and object
# --------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


s1 = Student("Samarth", 21)
print(s1.introduce())


# --------------------------------------------------
# Commit: Instance vs Class variables
# --------------------------------------------------

class College:
    college_name = "XYZ Engineering College"   # Class variable

    def __init__(self, student_name):
        self.student_name = student_name      # Instance variable

    def show(self):
        print(f"{self.student_name} studies in {College.college_name}")


c1 = College("Samarth")
c1.show()


# --------------------------------------------------
# Commit: Encapsulation (private variables)
# --------------------------------------------------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(5000)
acc.deposit(2000)
print("Bank Balance:", acc.get_balance())


# --------------------------------------------------
# Commit: Inheritance
# --------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")


class Engineer(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch

    def details(self):
        print(f"{self.name} is an engineer in {self.branch}.")


e1 = Engineer("Samarth", "Computer Science")
e1.greet()
e1.details()


# --------------------------------------------------
# Commit: Polymorphism (method overriding)
# --------------------------------------------------

class Animal:
    def sound(self):
        print("Some generic sound")


class Dog(Animal):
    def sound(self):
        print("Bark Bark!")


a = Animal()
d = Dog()

a.sound()
d.sound()


# --------------------------------------------------
# Commit: Abstraction using Abstract Class
# --------------------------------------------------

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car is starting with key!")


c = Car()
c.start()


# --------------------------------------------------
# Commit: Mini real-world OOP example – Library System
# --------------------------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.info())


b1 = Book("Atomic Habits", "James Clear")
b2 = Book("Python Basics", "Samarth")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

print("Library Books:")
lib.show_books()


# --------------------------------------------------
# Commit: End of Day 12 – OOP completed
# --------------------------------------------------

print("=== Day 12 Completed Successfully ===")
