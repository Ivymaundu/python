# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only
# or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .

number1 = float(input("Enter number: "))
number2 = float(input("Enter number: "))


if (type(number1))=="float" or (type(number2))=="float":
    sum = "Invalid character entered"
else:
    sum = sum
print(sum)
