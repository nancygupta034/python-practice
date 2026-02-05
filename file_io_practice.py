#Ek text file data.txt banao aur "Hello Python" likho.
file = open("data.txt", "w")
file.write("Hello Python")
file.close()

#File ko read karo aur content print karo.
file = open("data.txt", "r")
print(file.read())
file.close()

#File me append mode me "Welcome to Gen AI" add karo.
file = open("data.txt", "a")
file.write("\nWelcome to Gen AI")
file.close()

#File ka first line print karo.
file = open("data.txt", "r")
line = file.readline()
print(line)
file.close()

#File ka line count print karo.
file = open("data.txt", "r")
line_count = len(file.readlines())
print(line_count)
file.close()

#File me kitne words hain count karo.
file = open("data.txt", "r")
lines = file.read()
list = lines.split()
print(len(list))
file.close()

#File me kitne characters hain count karo (spaces included).
file = open("data.txt", "r")
lines = file.read()
print(len(lines))
file.close()

#File ke sab words ko uppercase me print karo.
file = open("data.txt", "r")
content = file.read()
uppercase_content = content.upper()
file = open("data.txt", "w")
file.write(uppercase_content)
file.close()

#File ke sab words ko new line me print karo.
file = open("data.txt", "r")
content = file.read()
modified_content = content.split()
file = open("data.txt", "w")
for i in modified_content:
    if i == modified_content[0]:
        file.write(i)
    else:
        file.write("\n"+i)

file.close()

#File ke content ko reverse order me print karo.
file = open("data.txt", "r")
content = file.read()
modified_content = content.split()
file = open("data.txt", "w")
for j in range(len(modified_content)-1, -1, -1):
    string = modified_content[j]
    for i in range(len(string)-1, -1, -1):
        file.write(string[i])
        i -= 1
    file.write(" ")
    j -= 1
    
file.close()

#2nd solution
with open("data.txt", "r") as file:
    lines = file.readlines()

with open("data.txt", "w") as file:
    for line in reversed(lines):
        file.write(line[::-1])


#File me "python" word search karo (case-insensitive).

#File me se sirf even length wale words print karo.

#File me se duplicate words remove karke new file me likho.

#File me se sirf wahi lines print karo jisme number ho.

#File me se emails extract karo.


# Ek file se content read karo aur doosri file me copy karo.

# Do files ko merge karke third file banao.

# File ke content ko line-by-line read karo using loop.

# File ko empty karo (without deleting file).

# Check karo file exist karti hai ya nahi.

# CSV file read karo aur data print karo.

# CSV file me se highest marks find karo.

# CSV file me se sirf pass students ko new file me likho.

# CSV file me ek new row add karo.

# CSV ko dictionary me read karo.

# Log file me se sirf ERROR lines extract karo.

# Word frequency program using file.

# File ka longest word find karo.

# File me se stop words remove karo.

# File ka backup banao with timestamp in filename.