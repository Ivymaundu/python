# Write a program called stars. It should prompt the user for a number, and it should print the number of 
# stars till the number entered.Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....

stars = int(input(("Enter number of rows: ")))
count=0
for i in range(1,stars):
    value=("*"*i)
    count+=1
    if count==stars:
        value+=("."*i)
    print(value)
