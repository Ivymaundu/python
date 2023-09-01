# Write a program that takes the date of birth of a person
# and the program outputs the age in terms of years,months,days TODAY.

import datetime
birth_date = int(input("Enter your birthday date: "))
birth_month = int(input("Enter your month of birth: "))
birth_year = int(input("Enter your year of birth: "))

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

day_difference = current_day-birth_date
month_difference = current_month-birth_month
year_difference = current_year-birth_year

print("Your current age is ",year_difference,"years",month_difference, "months",day_difference,"days")