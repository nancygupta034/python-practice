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



 
