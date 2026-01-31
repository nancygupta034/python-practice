#User se name aur age input lo, output: (Hello Rahul, you are 22 years old)
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old")

#Do numbers input lo aur unka sum, difference, product print karo.
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
print(f"sum is {sum} and diff is {difference} and product is {product}")

#Celsius input lo aur Fahrenheit me convert karo.
temp_in_celcius = int(input("Enter temperature in celcius: "))
temp_in_fahrenheit = (temp_in_celcius * 1.8) + 32
print(temp_in_fahrenheit)

#User se salary input lo, 10% bonus add karke final salary print karo.
salary = int(input("Enter your salary: "))
bonus = (0.1 * salary)
final_salary = salary + bonus
print(f"Final salary is {final_salary}")

#Radius input lo aur circle ka area print karo (π = 3.14).
radius = int(input("Enter radius: "))
area = (3.14 * (radius * radius))
print(area)