#User se ek string lo aur:
#uppercase
#lowercase
#length print karo

user_str = input("Enter string: ")
print(user_str.upper())
print(user_str.lower())
print(len(user_str))

#Check karo ki string "python" word contain karti hai ya nahi.
if 'python' in user_str:
    print("yes")
else:
    print("no")


#number of words count karo
word_count = 1
for i in user_str:
    if(i == " "):
        word_count += 1

print(f"word count is {word_count}")


#2 har word new line me print karo
for i in user_str.split():
       print(f"{i}") 

#String ka first aur last character print karo.
print(f"first char is {user_str[0]}")
print(f"last char is {user_str[-1]}")

#Input string me se vowels count karo.
vowel_list = ['a','e','i','o','u']
vowel_count = 0
for i in user_str:
    if i in vowel_list:
        vowel_count += 1
    
print(f"total vowels are {vowel_count}")

#Check karo string palindrome hai ya nahi.
user_str_copy = user_str[::-1]
if user_str == user_str_copy:
    print("string is palindrom")
else:
    print("not palidrome")