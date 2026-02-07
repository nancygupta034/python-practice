#LEVEL 1: BASICS (CLASS & OBJECT)
#Student class banao jisme: attributes: name, age method: display_info()
# class Student():
#     def __init__(self):
#         self.name = "Nancy"
#         self.age = 30

#     def display_info(self):
#         print(f"Name is {self.name} and age is {self.age}")


# student1 = Student()
# student1.display_info()

#Rectangle class banao: attributes: length, breadth methods: area(), perimeter()
# class Rectangle:

#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

    
#     def area(self):
#         return self.length * self.breadth
    
#     def perimeter(self):
#         return 2*(self.length + self.breadth)
    

# rect1 = Rectangle(21,11)
# print(rect1.area())
# print(rect1.perimeter())


# Car class banao: attributes: brand, model, price method jo price increase kare by 10%
# class Car:

#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def increasePrice(self):
#         self.price = ((10 * self.price)/100 + self.price)
#         return True


# car1 = Car("Toyota", "Fortuner", 20000)
# print(f"Old price is: {car1.price}")
# car1.increasePrice()
# print(f"Increased price: {car1.price}")


#Employee class banao: attributes: name, salary method jo annual salary calculate kare
# class Employee():
#     name = "Nancy"
#     salary = 52000

#     def annualSalary(self):
#         return 12 * self.salary
    

# emp1 = Employee()
# print(emp1.annualSalary())

#LEVEL 2: CONSTRUCTOR & INSTANCE METHODS
#BankAccount class banao: constructor me account_number, balance methods: deposit(), withdraw()
# class BankAccount():

#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amt):
#         self.balance = self.balance + amt
#         return True

#     def withdraw(self, amt):
#         self.balance = self.balance - amt
#         return True
    
#     def displayDetails(self):
#         print(f"Acc no. is {self.account_number} and balance is {self.balance}")
    

# acct1 = BankAccount(1263265262, 5000000)
# acct1.deposit(5000)
# acct1.withdraw(200)
# acct1.displayDetails()

#Book class banao: constructor with title, author method: get_details()
# class Book():
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def getDetails(self):
#         print(f"title is {self.title} and author is {self.author}")

# book = Book("knock knock", "NANON")
# book.getDetails()


#Mobile class banao: constructor: brand, price method jo discount apply kare
# class Mobile():
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price


#     def apply_discount(self, discount):
#         discount_baht = ((discount * self.price)/100)
#         return self.price - discount_baht
    
# mbl1 = Mobile("Samsung", 100000)
# print(mbl1.apply_discount(20))

#LEVEL 3: ENCAPSULATION
#User class banao: private attribute __password methods: set_password(), check_password()
# class User():
#     __password = ""

#     def set_password(self, password):
#         self.__password = password

#     def check_password(self, password):
#         if (self.__password == password):
#             print("Matched")
#         else:
#             print("Not matched")

    
# user1 = User()
# user1.set_password(12345678)
# user1.check_password(123456780)

#ATM class banao: private balance public methods for withdraw & balance check
# class ATM():
#     __balance = 1000000

#     def withdrawl(self, amt):
#         self.__balance -= amt

#     def checkBalance(self):
#         return self.__balance
    

# user1 = ATM()
# user1.checkBalance()
# print(f"current balance is {user1.checkBalance()}")
# user1.withdrawl(50000)
# print(f"new balance is {user1.checkBalance()}")

#Employee class banao: private salary getter & setter methods


#LEVEL 4: INHERITANCE

# Person class banao: attributes: name, age Student class inherit kare:  extra attribute: roll_no

# Animal class banao:  method: sound() Dog & Cat classes inherit kare aur sound override kare

# Vehicle → Car → ElectricCar Multi-level inheritance example

# LEVEL 5: POLYMORPHISM

# Same method name area() for:  Circle  Rectangle Triangle

# Method overriding example with parent & child class

# Function jo different objects ko accept kare aur same method call kare

# 🔴 LEVEL 6: ABSTRACTION (INTERVIEW FAVORITE)

# Abstract class Shape banao: abstract method area()

# Abstract class Payment pay() method Implement in UPI, Card

# ⭐ BONUS (REAL-WORLD THINKING)

# Library system:  Add book  Issue book  Return book

# E-commerce Product class: Apply discount Calculate final price

# Login System: User registration Password check
