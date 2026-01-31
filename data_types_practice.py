#Ek variable banao har data type ka (int, float, string, bool) aur type() print karo.
var1 = 1
var2 = 1.0
var3 = "nancy gupta"
var4 = True
var5 = [1,2,3,45,5]
var6 = (3,4,5,6,7,2)
var7 = {"name": "nancy", "age": 35}
var8 = {2,5,6,7,8,8}

print(f"{type(var1)}\n{type(var2)}\n{type(var3)}\n{type(var4)}\n{type(var5)}\n{type(var6)}\n{type(var7)}\n{type(var8)}\n")

#User se number input lo (string hoga), usko integer me convert karke square print karo.
user_input = input("Enter string value: ")
input_in_int = int(user_input)
print(input_in_int * input_in_int)

#Check karo ki input number int hai ya float (hint: decimal point).
input_number = input("Enter number: ")
if '.' in input_number:
    print("Float")
else:
    print("Int")