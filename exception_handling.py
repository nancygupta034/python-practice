#whenever an exception occur -> python goes to his class then call constructor and then raise message
try:
    age=int(input("Enter age: "))
    if age<0:
        raise ValueError
    print("Your age is: ",age)
except ValueError:
    print("Invalid age")

print("rest of code")

#OR you can do
try:
    age=int(input("Enter age: "))
    if age<0:
        raise ValueError("Invalid age")
    print("Your age is: ",age)
except ValueError as var:
    print(var)

print("rest of code")


#WAP for FiveDivisionError Exception
class FiveDivisionException(BaseException):
    pass

try: 
    n1=int(input("Enter first number"))
    n2=int(input("Enter second number:"))
    if n2==5:
        raise FiveDivisionException("Can not divided by 5")
    div = n1/n2
    print(f"Div is {div}")
except FiveDivisionException as msg:
    print(msg)

print("Rest of code")


#Excepthook
# the interpreter calls sys.excepthook() with three arguments: Exception class, Exception value and Exception traceback object
# this function prints out a given traceback and exception to sys.stderr 
import sys
def format_traceback(exec_type, exec_value, exec_traceback):
    print("Something went wrong.")
    print(exec_type)
    print(exec_value)
    print(list(exec_traceback))


sys.excepthook=format_traceback
def display():
    print(100+"hi")

display()
