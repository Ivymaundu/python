# Write a program which accepts email as form input or from terminal. 
# Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

mail = input("Enter your email: ")

if(mail.index('.') - mail.index('@')>1)  and (mail.index('@')>0) and (mail.index('.')+1>len(mail)):
        print("email is valid")
    
else:
       print("wrong email")