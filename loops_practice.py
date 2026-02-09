#1 se 10 tak numbers print karo.
i = 1
while i < 11:
    print(i)
    i += 1 

#10 se 1 tak numbers print karo.
print("10 se 1 tak numbers print karo.")
i = 10
while i > 0:
    print(i)
    i -= 1

#1 se 50 tak sirf even numbers print karo.
# print("----1 se 50 tak sirf even numbers print karo.------")
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
#     i += 1   

#1 se 50 tak sirf odd numbers print karo.
# print("-----1 se 50 tak sirf odd numbers print karo.------")
i = 1
for i in range(51):
    if i % 2 != 0:
        print(i)
#     i += 1

#List [10, 20, 30, 40, 50] ke sab elements print karo.
list = [10, 20, 30, 40, 50]
for i in range(len(list)):
#     print(list[i])

#String "python" ke har character ko new line me print karo.
str = "python"
i = 0
while i < len(str):
    print(str[i]) 
    i += 1

#List ka sum find karo using loop.
sum = 0
for i in list:
    sum += i

print(sum)


#Ye pattern print karo:
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print("*"*i)

# 1
# 12
# 123
# 1234
for i in range(1,5):
    for j in range(1, i+1):
        print(j, end="")
    print()
        

# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    print("*"*i)



#User se ek number lo aur uska table print karo.
number = int(input("Enter number: "))

for i in range(1, 11):
    print(number * i)
    i += 1

# User se ek number lo aur uska factorial nikalo.
number = int(input("Enter number: "))
factorial = 1
for i in range(number, 0, -1):
    factorial *=  i

# print(f"factorial is {factorial}")

# Given list me se maximum element find karo (without max()).
list = [25,23,12,42,56,93,98,56,75]
max = list[0]
i = 0
while i < len(list):
    if (list[i] > max):
        max = list[i]
    
    i += 1

print(f"Max value from list is {max}") 

# Count karo ki list me kitne even numbers hain.
list = [25,23,12,42,56,93,98,56,75]
count =  0
i = 0
while i < len(list):
    if list[i] % 2 == 0:
        count += 1
    
    i += 1

print(f"count of even number in list is {count}") 

# User se string lo aur vowels count karo.
string = input("Enter any string in which you want to count vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
i = 0
while i < len(string):
    if string[i] in vowels:
        count += 1

    i += 1

print(f"count of vowels in string is {count}") 


# String ko reverse karo using loop (without slicing).
string = input("Enter any string which you want to reverse: ")
reversed = ""

for i in range(len(string)-1, -1, -1):
    reversed += string[i]

print(f"Reversed string is: {reversed}")

# List me se duplicate elements remove karo.
list = [12,25,16,23,25,12,65,18,45,12,65,16]
unique_list = []

for i in range(i, len(list)):
    if list[i] not in unique_list:
        unique_list.append(list[i])

print(f"Unique list is: {unique_list}")

# Multiplication tables from 1 to 5 print karo.
for i in range(1, 6):
    print(f"Multiple table of {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")

# 1 se 10 tak numbers print karo using while loop.
i = 1
while i < 11:
    print(i)
    i += 1

# User se numbers input lete raho jab tak wo 0 enter na kare.
number = 1
while number != 0:
    number = int(input("Enter number: "))

Guess the number game (fixed number = 7).
fixed_number = 7
number = 0
while number != fixed_number:
    number = int(input("Guess the number: "))
    if fixed_number > number:
        print("Too low, try again")
    elif fixed_number < number:
        print("Too high, try again")

print("Congratulations, you guessed it!")

# Number ka digit count find karo.
number = input("Enter number: ")
print(len(number))

# Number ka sum of digits find karo.
number = int(input("Enter number: "))
sum = 0

while number != 0:
    sum = sum + (number % 10)
    number  = number // 10

print(f"Sum of digit is: {sum}")  

# Check karo number prime hai ya nahi.
number = int(input("enter number: "))
i = 2
is_prime = True
while i < number:
    if number % i == 0:
        is_prime =  False
    i += 1

if is_prime == True:
    print("Prime number")
else:
    print("Not prime number")

# Fibonacci series print karo (n terms).
length = int(input("Enter the length of series: "))
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
i = 0
list = [first,second]
while i < length:
    next = list[len(list) - 1] + list[len(list) - 2]
    list.append(next)
    i += 1

print(f"Fibnocci series of {length}th items is: {list}")


# Check karo number palindrome hai ya nahi.
number = input("Enter number: ")
reversed = ""
i = len(number) - 1
while i >= 0:
    reversed += number[i]
    i -= 1

if number == reversed:
    print("Palidrome")
else:
    print("Not palidrome")


# List me second largest element find karo.
list = [21,26,56,25,85,96,54]
for i in range(0,len(list)):
    for j in range(i+1, len(list)):
        if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print(f"sorted list is: {list} and second highest number is {list[1]}")

# String me har character ki frequency count karo (dictionary + loop).
string = input("Enter string: ")
i = 0
dict = {}
keys = dict.keys()
while i < len(string):
    if string[i] in keys:
        dict[string[i]] += 1
    else:
        dict[string[i]] = 1
    i += 1

print(f"frequency of each character is: {dict}")

# Armstrong number check karo.
number = input("Enter number: ")
sum = 0

for i in range(0,len(number)):
        sum += int(number[i]) ** len(number) 

print(sum)

# Given list ko reverse karo without reverse() or slicing
list = [21,26,56,25,85,96,54]
reversed = []

for i in range(len(list)-1, -1, -1):
    reversed.append(list[i])

print(reversed)

# Sentence ke har word ko new line me print karo.
sentence = input("Enter sentence: ")
word = ""
for i in sentence:
    if i != " ":
        word += i 
    else:
        print(word)
        word = ""

print(word)

# Longest word find karo from sentence.
sentence = input("Enter sentence: ")
list = sentence.split(" ")
max = 0
longest = ""
dict = {}
for word in list:
    if len(word) > max:
        max = len(word)
        longest = word

print(longest)


# Remove extra spaces from string using loop.
s = "  Hello   world   Python  "
result = ""
space_found = False

for ch in s:
    if ch != " ":
        result += ch
        space_found = False
    elif not space_found and result != "":
        result += ch
        space_found = True

print(result)

# List ko flatten karo: [[1,2],[3,4],[5,6]] → [1,2,3,4,5,6]
nested = [[1,2],[3,4],[5,6]]
result = []

for item in nested:
    if isinstance(item, list):
        for i in item:
            result.append(i)

    else:
        result.append(item)

print(result)


#2nd method:
nested = [[1,2],[3,4],[5,6]]
result = [i for item in nested for i in item]
print(result)
 
