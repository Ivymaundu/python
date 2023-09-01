# Write a program that prints the largest of 4 inputs taken in from a user.
# Assume that the user would not enter any two numbers which are the same.

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))
num4 = float(input("Enter 4th number: "))

if num1>num2 and num1>num3 and num1>num4:
    largest_number = num1
elif num2>num1 and num2>num3 and num2>num4:
    largest_number = num2
elif num3>num1 and num3>num2 and num3>num4:
    largest_number = num3
elif num4>num1 and num4>num2 and num4>num3:
    largest_number = num4
else:
    largest_number = "Enter a valid number"

print(largest_number)
