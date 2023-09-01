# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” 
# and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”.
# ONLY accept 3 tries after which it notifies you that you have been blocked.


email = "admin@mail.com"
pass_word  = "Admin@123"

for i in range(1,4):
    user_email = input("Enter email: ")
    user_password = input("Enter password: ")
    if user_email==email and user_password==pass_word:
        status = "Login Succesful"
        break
    else:
        status = "Account blocked,try again after a while"
print(status)