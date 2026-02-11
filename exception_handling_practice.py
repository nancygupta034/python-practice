#LEVEL 1 – BASIC TRY / EXCEPT
# User se number lo aur divide by 10 karo. -> Agar user string daal de toh error handle karo.
try:
    number = int(input("Enter number: "))
    div = number /10
    print(div)
except:
    print("Enter valid number")

#Better Version: (ValueError specifically tab aata hai jab string ko int me convert nahi kar paate.)
try:
    number = int(input("Enter number: "))
    div = number / 10
    print(div)
except ValueError:
    print("Enter valid number")

# 2 numbers lo aur divide karo. -> ZeroDivisionError handle karo.
try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError("Cannot be divided by zero")
    div = num1/num2
    print(div)
except ZeroDivisionError as msg:
    print(msg)

#Better Version: (Python khud ZeroDivisionError raise karta hai — manually check karne ki zarurat nahi thi.)
try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter valid numbers")

# List me se index input lo aur element print karo. -> IndexError handle karo.
try:
    list = [21,25,56,85,6]
    index = int(input("Enter index: "))
    if index not in range(-len(list), len(list)):
         raise IndexError("Out of index")
    print(list[index])
except IndexError  as msg:
    print(msg)

#Better Version: Manual range check unnecessary hai. Python already IndexError deta hai and list naam mat use karo — yeh Python ka built-in function hai.Isko override karna bad practice hai.
my_list = [21,25,56,85,6]

try:
    index = int(input("Enter index: "))
    print(my_list[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Enter valid index number")

# Dictionary me se key input lo. -> Agar key exist na kare toh handle karo.
dictionary = {"name": "nancy", "age": 30, "location": "thailand"}
try:
    key = input("Enter key: ")
    dict_keys = dictionary.keys()
    if key not in dict_keys:
        raise IndexError("Out of index")
    print(dictionary[key])
except IndexError as msg:
    print(msg)


#Best Version: Dictionary me key missing hone par IndexError nahi, KeyError use hota hai. and dict_keys = dictionary.keys() unnecessary hai.
dictionary = {"name": "nancy", "age": 30, "location": "thailand"}

try:
    key = input("Enter key: ")
    print(dictionary[key])
except KeyError:
    print("Key does not exist")


#LEVEL 2 – MULTIPLE EXCEPT BLOCKS
# Program banao jo: 1. number input le 2. list access kare 3. divide kare -> Handle: ValueError, IndexError, ZeroDivisionError
# Ek program likho jo file open kare. -> Agar file exist na kare toh FileNotFoundError handle karo.

#LEVEL 3 – ELSE & FINALLY
# 2 numbers divide karo: Agar error nahi aaye → result print karo (else) / Finally me print karo: "Program finished"
# File open karo, read karo, finally me close karo.

#LEVEL 4 – CUSTOM EXCEPTION
# Custom exception banao: InvalidAgeError -> Condition: Age < 18 → raise exception

# Password check system: Password length < 6 → custom exception raise karo

#LEVEL 5 – RAISE KEYWORD
#Function banao jo negative number accept na kare -> Agar negative aaye → raise ValueError
#Bank withdrawal: -> Agar withdraw amount balance se zyada ho → raise Exception

#LEVEL 6 – REAL-WORLD SCENARIO
#Login system: Username galat, Password galat, 3 attempts ke baad account block
#Calculator: Invalid operator, Zero division, Non-numeric input
#API-like simulation:-> Function data fetch kare -> Agar data None ho → custom error raise karo

#BONUS – INTERVIEW THEORY
#1. Difference between Error & Exception?
#2. try-except-else-finally ka flow?
#3. finally kab execute hota hai?
#4. raise ka use kyun karte hain?
#5. Custom exception kyun useful hai?
#6. Python me Exception hierarchy kya hoti hai?


#Mini Project banao:
#ATM System with proper exception handling
    #Invalid pin
    #Insufficient balance
    #Invalid amount input