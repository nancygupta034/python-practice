#Ek function banao jo two numbers ka sum return kare.
def sum(a, b):
    return a+b

print(sum(2,6))

#Function banao jo name input le aur greeting print kare.
def greet(name):
    print(f"Good morning, {name}!")

name = input("Enter name: ")
greet(name)

#Function banao jo number even ya odd check kare.
def check_number(number):
    if (number %  2 == 0):
        print("even")
    else:
        print("odd")

check_number(int(input("Enter number: ")))

#Function banao jo list ka sum return kare.
list  = [25,26,45,63,85]
sum = 0
def list_sum(sum1, num):
    sum1 += num
    return sum1

i = 0
while i < len(list):
    sum = list_sum(sum, list[i])
    i += 1

print(f"sum is :{sum}")

#Function banao jo string length return kare.
str = "python"

def count_str(str):
    count = 0
    for i in str:
        count += 1

    return count

print(count_str(str))

# Function banao jo maximum of three numbers return kare.

# Function banao jo Celsius → Fahrenheit convert kare.

# Function banao jo factorial calculate kare (without recursion).

# Function banao jo count vowels in string.

# Function banao jo list me se duplicates remove kare.

#Function banao: -> def student_info(name, age=18): Output:-> Name: Rahul, Age: 18

# Function banao jo keyword arguments accept kare aur sab print kare.

# Function banao jo simple interest calculate kare using default rate = 5%.

# Function banao jo prime number check kare.

# Function banao jo palindrome string check kare.

# Function banao jo second largest element find kare.

# Function banao jo dictionary me highest value ka key return kare.

# Function banao jo string reverse kare without slicing.

# Recursive function banao jo 1 se n tak numbers print kare.

# Recursive function banao jo factorial calculate kare.

# Recursive function banao jo sum of n natural numbers calculate kare.

# Recursive function banao jo countdown kare (n → 1).

# Recursive function banao jo Fibonacci series ka nth term return kare.

# Recursive function banao jo string reverse kare.

# Recursive function banao jo list ka sum calculate kare.

# Recursive function banao jo power (xⁿ) calculate kare.

# Recursive function banao jo number palindrome check kare.

# Recursive function banao jo count digits in number.

# Recursive function banao jo binary search implement kare.

# Recursive function banao jo GCD (HCF) find kare using Euclid algorithm.

# Recursive function banao jo nested list ko flatten kare.

# Recursive function banao jo string se spaces remove kare.

# Recursive function banao jo dictionary ke values ka sum kare.
    
