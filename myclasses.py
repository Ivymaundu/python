# x=0
# def myincreament():
#     print("x0 is: ",x)
#     x=x+1
#     return x

# x = myincreament()
# print("x1 is : ",x)

# classes are a collection of functions and variables that are created and can manipulate each other
# a function inside a class is called a method
# representation of something in the realworld
# Example student
# here you have all functions and properties related to a student eg create_student(),email()

class Person():
    name=""
    gender=""
    email=""
    phone=""
    details=[]
# Constructor- Aspecial method used to instantiate initial values
    def __init__(self,n,g,e,p):
        self.name = n
        self.gender = g
        self.email = e
        self.phone = p
        self.add()

    def add(self):
        self.details.append(self.name)
        self.details.append(self.gender)
        self.details.append(self.email)
        self.details.append(self.phone)
    
p = Person(input("Enter name: "),
           input("Enter gemder: "),
           input("Enter email: "),
           input("Enter phone: "))
print(p.details)

