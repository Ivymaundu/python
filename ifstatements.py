# age = int(input("what age are you ?"))

# if (age < 18) :
#     print("you have not yet reached the voting age")
# else:
#     print("you are eligible for voting")


    # taking data from a user and determining which number is the largest

# num1 = float(input("enter number: "))
# num2 = float(input("enter number: "))
# num3 = float(input("enter number: "))

# if (num1 >num2 and num1>num3):
#     print("largest number is ",num1)
# elif(num2>num1 and num2>num3):
#     print("largest number is ",num2)
# else:
#     print("largest number is ",num3)


# program for checking if a number is divisible by 7
# num = int(input("Enter your number: "))
# if num%7 == 0:
#     print("number is divisible by 7")
# else:
#     print("number is not divisible by 7")

# program to calculate the electricity bill based on following criteris
# first 50 units            ksh.20
# next 50 units             ksh.40
# after 100 units           ksh.100

# units = float(input("Enter your units: "))
# if units>0 and units<=50:
#     print("your electricity bill is: kshs20")
# elif units>50 and units<=100:
#     print("your electricity bill is: kshs40")
# else:
#     print("your electricity bill is: kshs100")


# 1.Given a variable temperature with a value of 25°C, write an if statement 
# to check if the temperature is above 30°C using the greater than (>) operator.


# temperature = 25
# if temperature>30:
#     print("Temperature is greater than 30°C")
# else:print("Temperature is less than 30°C")

# 2.	Create a dictionary called stock with items as keys and their quantities as values.
#  Write an if-else statement to check if the quantity of "apples" is zero 
# using the equality (==) operator. 

# stock = {"mangoes":10,"Apples":70,"Oranges":50}
# if stock["Apples"]==0:
#     print("True")
# else:
#     print("False")

# 3.Declare a list called even_numbers containing integers. 
# Write an if statement to check if the first element of the list is 
# an even number using the modulo (%) operator 

# even_numbers = [1,5,7,8,3,30,50]

# if even_numbers[0]%2==0:
#     print("even number")
# else:
#     print("first number is odd")

# 4. Given a list prices containing prices of products,
# write a code snippet using if statements to check if 
# any product's price is within the range $20 to $50 using the logical and operator.

# 4.Imagine you have a list employees containing dictionaries with keys "name",
#  "hours_worked", and "hourly_rate". Write a code snippet using nested if statements
#  to calculate the salary for an employee named "Alice" based on her hours worked 
#  and hourly rate.

# employees = [{"name":"Alice","hours_worked":7,"hourly_rate":200},
#              {"name":"Jane","hours_worked":4,"hourly_rate":200},
#              {"name":"Fabiola","hours_worked":10,"hourly_rate":200}]

# if employees[0]["name"] =="Alice":
#     print("Alice exists")
# else:
#     print("Alice does not exist")

# hours_worked =float( employees[0]["hours_worked"])
# hourly_rate = float(employees[0]["hourly_rate"])
# salary = hours_worked * hourly_rate
# print(round(salary))

# 5.	Create a dictionary book_ratings with book titles as keys and 
# their ratings as values. Write an if-elif-else 
# statement to find out if a book "The Adventure" has a rating of 5 or is rated below 2.

# book_ratings = {"Beauty and the beast":8,"The adventure": 1,"Master":1}

# if book_ratings["The adventure"]==5:
#     print("has a rating of 5") 
# elif book_ratings["The adventure"]<2:
#     print("it's rated below 2")
# else:
#     print("has a rating of above 5")

# 6.	Suppose you have two sets: set_x and set_y. Write a code snippet 
# using conditional statements to check if the symmetric difference between 
# the two sets is not empty, using the ^ (symmetric difference) operator

set_x = {50,51,52,53,53}
set_y = {40,41,52,43,44}
set_z = set_x^set_y

if set_z=={}:
    print("The symmetric difference between set_x and set_y is empty")
else:
    print("The symmetric difference between set_x and set_y is not empty")