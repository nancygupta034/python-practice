#Ek dictionary banao:
student = {"name": "Amit", "age": 21, "marks": 85}

#aur values print karo.
print(f"values of student dictionary are: {student.values()}")


#User se name aur marks input lo, dictionary me store karo.
name = input("Enter the name:")
marks = int(input("Enter the marks:"))
student.update({"name": name, "marks": marks})
print(f"Updated dictionary is: {student}")

#Dictionary me highest marks wale student ka name print karo.
max_marks = 0
topper = ""
dict1 = {"pooja": 100, "nnc": 99, "xyz": 56}
for name, marks in dict1.items():
    if marks > max_marks:
        max_marks = marks
        topper = name
    
print(f"topper namre is {topper} and his marks are {max_marks}")

#Word frequency program:
sentence = "hello world hello python"
dic2 = {}

for word in sentence.split():
    if word in dic2.keys():
        dic2[word] += 1
    else:
        dic2[word] = 1


print(f"Here is the updated dictionary: {dic2}")