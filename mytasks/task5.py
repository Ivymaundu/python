# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. 
# Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

if num1>num2 and num1>num3:
    print(num1,"is greatest")
elif num2>num1 and num2>num3:
    print(num2,"is greatest")
elif num3>num1 and num3>num2:
    print(num3,"is greatest")
else:
    print("all numbers are equal")