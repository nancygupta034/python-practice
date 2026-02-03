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
print("----1 se 50 tak sirf even numbers print karo.------")
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1   

#1 se 50 tak sirf odd numbers print karo.
print("-----1 se 50 tak sirf odd numbers print karo.------")
i = 1
for i in range(51):
    if i % 2 != 0:
        print(i)
    i += 1

#List [10, 20, 30, 40, 50] ke sab elements print karo.
list = [10, 20, 30, 40, 50]
for i in range(len(list)):
    print(list[i])

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
# User se ek number lo aur uska factorial nikalo.
# Given list me se maximum element find karo (without max()).
# Count karo ki list me kitne even numbers hain.
# User se string lo aur vowels count karo.
# String ko reverse karo using loop (without slicing).
# List me se duplicate elements remove karo.
# Multiplication tables from 1 to 5 print karo.
# 1 se 10 tak numbers print karo using while loop.
# User se numbers input lete raho jab tak wo 0 enter na kare.
# Guess the number game (fixed number = 7).
# Number ka digit count find karo.
# Number ka sum of digits find karo.
# Check karo number prime hai ya nahi.
# Fibonacci series print karo (n terms).
# Check karo number palindrome hai ya nahi.
# List me second largest element find karo.
# String me har character ki frequency count karo (dictionary + loop).
# Armstrong number check karo.
# Given list ko reverse karo without reverse() or slicing
# Sentence ke har word ko new line me print karo.
# Longest word find karo from sentence.
# Remove extra spaces from string using loop.
# List ko flatten karo: [[1,2],[3,4],[5,6]] → [1,2,3,4,5,6]



 
