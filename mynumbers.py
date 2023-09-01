# + (addition operator) Example: x = 2  y = 5   z = x + y 
x=2
y=5
z=x+y
print(z)

# -  (Subtraction operator) Example: x = 2  y = 5    x - y = -3
x=2
y=5
z=x-y
print(z)
# *  (Multiplication operator) Example: x = 2  y = 5   x * y = 10
x=2
y=5
z=x*y
print(z)
# / (Division operator) Example: x = 2  y = 5   x / y = 0.4
x=2
y=5
z=x/y
print(z)
# ** (Exponential operator) Example: x = 2   y = 5   x ** y = 32	
x=2
y=5
z=x**y
print(z)
# % (Modulo operator - This is the remainder of division)
# Example: x = 2  y = 5   y % x = 1
x=2
y=5
z=x%y
print(z)
# // (Floor operator - Division that result into whole numbers)
# Example: x = 30  y = 7   x // y = 4
x=50
y=3
z=x//y
print(z)

# Convert a float to an integer with an inbuilt function in Python
temp = 56.8926 
print(temp.__round__())

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89
temp = 56.8926
print(temp.__round__(2))

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp = 56.8926
print(temp.__round__(3))
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
temp = 56.8926
# NB: Use string  slice & concatenation, but have result as float 
s = 'colorless'
s_two = ''
s_two = s[0:4] + 'u' + s[4:]
print(s_two)


