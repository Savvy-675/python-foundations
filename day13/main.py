"""
===========================
Day 13: Advanced OOP in Python
Author: Samarth
===========================
"""

# --------------------------------------------------
# Commit: Initialize Day 13 – Advanced OOP
# --------------------------------------------------

print("=== Day 13: Advanced OOP ===")


# --------------------------------------------------
# Commit: Dunder methods (__str__ and __repr__)
# --------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


p = Person("Samarth", 21)
print(str(p))
print(repr(p))


# --------------------------------------------------
# Commit: Operator Overloading (__add__)
# --------------------------------------------------

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


n1 = Number(10)
n2 = Number(20)
n3 = n1 + n2
print("10 + 20 =", n3)


# --------------------------------------------------
# Commit: Class method and Static method
# --------------------------------------------------

class Student:
    school = "Modern College"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def is_adult(age):
        return age >= 18


print("Adult?", Student.is_adult(20))
Student.change_school("Tech University")
print("Updated school:", Student.school)


# --------------------------------------------------
# Commit: Property decorator (getter & setter)
# --------------------------------------------------

class Account:
    def __init__(self, balance):
        self._balance = balance   # protected variable

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = amount


acc = Account(5000)
print("Balance:", acc.balance)
acc.balance = 8000
print("Updated Balance:", acc.balance)


# --------------------------------------------------
# Commit: Multiple Inheritance
# --------------------------------------------------

class Father:
    def traits(self):
        print("Hardworking")

class Mother:
    def traits(self):
        print("Caring")

class Child(Father, Mother):   # Father method will be chosen first (MRO)
    pass

c = Child()
c.traits()


# --------------------------------------------------
# Commit: Method Resolution Order (MRO)
# --------------------------------------------------

print("MRO of Child:", Child.mro())


# --------------------------------------------------
# Commit: Real-world Mini Project – ATM System (OOP)
# --------------------------------------------------

class ATM:
    def __init__(self, pin, balance=10000):
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin

    def withdraw(self, entered_pin, amount):
        if not self.verify_pin(entered_pin):
            return "Incorrect PIN!"

        if amount > self.__balance:
            return "Insufficient Balance!"

        self.__balance -= amount
        return f"Withdrawn: ₹{amount}. Remaining: ₹{self.__balance}"

    def check_balance(self, entered_pin):
        if not self.verify_pin(entered_pin):
            return "Incorrect PIN!"
        return f"Balance: ₹{self.__balance}"


atm = ATM(pin=1234)

print(atm.check_balance(1234))
print(atm.withdraw(1234, 2000))
print(atm.check_balance(1234))


# --------------------------------------------------
# Commit: End of Day 13 – Advanced OOP completed
# --------------------------------------------------

print("=== Day 13 Completed Successfully ===")
