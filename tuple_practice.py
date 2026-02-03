#Ek tuple banao aur uska length print karo.
tup = (1,4,2,55,3,65,33)
print(len(tup))

#Tuple se max aur min element find karo.
min = tup[0]
max = tup[0]
for i in tup:
    if min > i:
        min = i

    if max < i:
        max = i

print(f"max is {max} and min is {min}") 


#Tuple ko list me convert karo, update karo, wapas tuple banao.
list = list(tup)
list.append(2555)
tup2 = tuple(list)

print(f"new tupke is: {tup2}")