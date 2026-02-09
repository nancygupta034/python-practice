#string in python

str = "i am studying python from apnacollege"
print(str.capitalize())
print(str.replace("o","a"))
#first_name = input("Enter your first name: ")
#print(len(first_name))
sttr = "$hi, iam $nancy$$gupta. i earn in $dollar USD$$$$ $$"
print(sttr.count('$'))


#Conditional Statements
marks = int(input("Enter the marks you got: "))
if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
else:
    grade = "D"

print(f"Your grade is: {grade}")
