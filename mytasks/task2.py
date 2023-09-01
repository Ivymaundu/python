# Prompt the user for a number either on a form input or the terminal.
# Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2?

number = (int(input("Enter your number: ")))

if number%2==0:
    print(number,"is an even number")
else:
    print(number,"is odd")