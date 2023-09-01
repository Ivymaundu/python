# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking 
# if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

phone_number = input("Enter phone number: ")


if(phone_number.startswith("+254")) and (len(phone_number)==13):
        print(phone_number)
    
elif(phone_number.startswith("07"))and (len(phone_number)==10):
        print("+254" + phone_number[1:])

elif(phone_number.startswith("01"))and (len(phone_number)==10):
        print("+254" + phone_number[1:])
        
elif(phone_number.startswith("7")) and (len(phone_number)==9):
        print("+254" +phone_number)
    
elif(phone_number.startswith("254")) and (len(phone_number)==12):
        print("+" +phone_number)
else:
        print("Not a number")
