# #Ek function banao jo two numbers ka sum return kare.
# def sum(a, b):
#     return a+b

# print(sum(2,6))

# #Function banao jo name input le aur greeting print kare.
# def greet(name):
#     print(f"Good morning, {name}!")

# name = input("Enter name: ")
# greet(name)

# #Function banao jo number even ya odd check kare.
# def check_number(number):
#     if (number %  2 == 0):
#         print("even")
#     else:
#         print("odd")

# check_number(int(input("Enter number: ")))

# #Function banao jo list ka sum return kare.
# list  = [25,26,45,63,85]
# sum = 0
# def list_sum(sum1, num):
#     sum1 += num
#     return sum1

# i = 0
# while i < len(list):
#     sum = list_sum(sum, list[i])
#     i += 1

# print(f"sum is :{sum}")

# #Function banao jo string length return kare.
# str = "python"

# def count_str(str):
#     count = 0
#     for i in str:
#         count += 1

#     return count

# print(count_str(str))

# # Function banao jo maximum of three numbers return kare.
# def maximum_number(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3
    
# print(maximum_number(25,12,65))

# # Function banao jo Celsius → Fahrenheit convert kare.
# def celsius_to_fahrenheit(temperature):
#     fah_temp = ((temperature * 1.8) + 32)
#     return fah_temp

# temp_in_cel = int(input("Enter temperature in celsius: "))
# print(celsius_to_fahrenheit(temp_in_cel))


# # Function banao jo factorial calculate kare (without recursion).
# def get_factorial(fact, num):
#     return fact * num

# number = int(input("Enter number: "))
# fact = 1
# for i in range(1, number+1):
#     fact = get_factorial(fact, i)

# print(fact)


# # Function banao jo count vowels in string.
# string = input("Enter string: ")
# def count_vowels(string):
#     list = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for char in string:
#         if char in list:
#             count += 1

#     return count

# print(count_vowels(string))

# # Function banao jo list me se duplicates remove kare.
# list1 = [25,66,85,95,25,66,2,5,85,2]

# def remove_duplicate(list1):
#     unique_list = []
#     for i in list1:
#         if i not in unique_list:
#             unique_list.append(i)

#     return unique_list

# print(remove_duplicate(list1))

# #2nd method
# unique = list(dict.fromkeys(list1))
# print(unique)

# # Function banao: -> def student_info(name, age=18): Output:-> Name: Rahul, Age: 18
# def student_info(name, age=18):
#     print(f"Name: {name}, Age: {18}")

# student_info("Rahul")

# # Function banao jo keyword arguments accept kare aur sab print kare.
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_kwargs(name="Nancy", age=25, city="Delhi")

# # Function banao jo simple interest calculate kare using default rate = 5%.
# def cal_si(principal, time, rate=5):
#     interest = ((principal * rate * time)/100)
#     return interest


# print(cal_si(1000,5))

# # Function banao jo prime number check kare.
# def check_prime(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False

#     return is_prime

# print(check_prime(5))

# # Function banao jo palindrome string check kare.
# def check_palidrome(number):

#     #if number is in string
#     reversed = ""
#     for i in range(len(number)-1, -1, -1):
#         reversed += str(number[i])

#     if number == reversed:
#         return True
#     else: 
#         return False
    
# #ToDo: what if number is not in string then what   
# print(check_palidrome("1223523221"))

# # Function banao jo second largest element find kare.
# def second_largest(list):
#     for i in range(0,len(list)):
#         for j in range(i,len(list)):
#             if list[j] > list[i]:
#                 temp = list[i]
#                 list[i] = list[j]
#                 list[j] = temp

#     return list[1]

# list = [23,26,52,98,55,75,35]
# print(second_largest(list))       

# # Function banao jo dictionary me highest value ka key return kare.
# dic = {"apple": 20, "bananc": 56, "chiku": 12, "grapes": 65}

# def get_highest(dic):
#     highest = 0
#     value = ""
#     for key in dic:
#         if dic[key] > highest:
#             highest = dic[key]
#             value = key

#     return value

# print(get_highest(dic))

# # Function banao jo string reverse kare without slicing.
# def reverse_string(string):
#     reversed = ""
#     for i in range(len(string)-1, -1, -1):
#         reversed += string[i]

#     return reversed

# print(reverse_string(input("Enter string: ")))

# Recursive function banao jo 1 se n tak numbers print kare.
# def print_number(current, n):
#     if current > n:
#         return
    
#     print(current,end="\n")
#     current += 1
#     print_number(current, n)

# limit = int(input("Enter nth number: "))
# print_number(1, limit)

# Recursive function banao jo factorial calculate kare.
def get_factorial(number):
    
    if number < 2:
        return 1
    
    factorial = (number * factorial)
    get_factorial(number - 1)

print(get_factorial(4))


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
    
