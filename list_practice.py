#Ek list banao numbers ki aur:
list = [2,5,66,4,25,85,11]

#sum print karo
sum = 0
for i in list:
    sum += i

print(f"sum is {sum}")

#max print karo
max = list[0]
for i in list:
    if i > max:
        max = i

print(f"max value in list is {max}")

#min print karo
min = list[0]
for i in list:
    if i < min:
        min = i

print(f"min value in list is {min}")

#User se 5 numbers lo aur list me store karo.
i = 0
for i in range(5):
    list.append(int(input()))
    i += 1

print(f"updated list is: {list}")

#List me se duplicate elements remove karo.
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)

#Second largest element find karo
list.sort(reverse=True)
print(f"second highest elemenet is {list[1]}")

#List ko reverse karo without using reverse() or slicing.
i = len(list) - 1
reversed_list = []
while i >= 0:
    reversed_list.append(list[i])
    i -= 1


print(f"reversed list is {reversed_list}")


#Two lists ko merge karo without
first_list = [12,45,65,25,23,42,21,26,85,98]
second_list = [6,5,2,4]
third_list = first_list

for i in second_list:
    third_list.append(i)

print(f"merged list is {third_list}")