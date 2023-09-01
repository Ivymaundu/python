# Write a program that takes input of someone's basic salary and benefits,
# adds them to find the gross salary then uses  the gross salary to find the NHIF

basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))

gross_salary = basic_salary + benefits

nhif = 0
if (gross_salary <= 5999) :
    nhif = 150

elif (gross_salary >= 6000 and gross_salary <= 7999) :
    nhif = 300

elif (gross_salary >= 8000 and gross_salary <= 11999) :
    nhif = 400
elif (gross_salary >= 12000 and gross_salary <= 14999) :
    nhif = 500

elif (gross_salary >= 15000 and gross_salary <= 19999) :
    nhif= 600

elif (gross_salary >= 20000 and gross_salary <= 24999) :
    nhif = 750

elif (gross_salary >= 25000 and gross_salary <= 29999):
    nhif = 850

elif (gross_salary >= 30000 and gross_salary <= 34999) :
    nhif = 900

elif (gross_salary >= 35000 and gross_salary <= 39999) :
    nhif = 950

elif (gross_salary >= 40000 and gross_salary <= 44999) :
    nhif = 1000

elif (gross_salary >= 45000 and gross_salary <= 49999) :
    nhif = 1100

elif (gross_salary >= 50000 and gross_salary <= 59999) :
    nhif = 1200

elif (gross_salary >= 60000 and gross_salary <= 69999) :
    nhif = 1300

elif (gross_salary >= 70000 and gross_salary <= 79999) :
    nhif = 1400

elif (gross_salary >= 80000 and gross_salary <= 89999) :
    nhif = 1500

elif (gross_salary >= 90000 and gross_salary <= 99999) :
    nhif = 1600

else :
    nhif = 1700
           
print("NHIF: ",nhif)



# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary.
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 


nssf = 0
rate = 0.06
if (gross_salary > 0 and gross_salary <= 18000) :
    nssf = (gross_salary * rate)
else :
    nssf = 18000 * rate
    
print("NSSF: ",nssf)


# Continue with the same program and calculate an individual’s NHDF using:i.e NHDF = gross_salary *  0.015
nhdf = 0
amount = 0.015
if(gross_salary <= 83333):
    nhdf = gross_salary * amount
else :
    nhdf =2500

print("NHDF: ",nhdf)

# nssf +nhdf

# Calculate the taxable income.i.e taxable_income = gross salary - (NSSF + NHDF) 
taxable_income = gross_salary-(nssf+nhdf)
print("TAXABLE INCOME: ",taxable_income)



# Continue with the same program and find the person's PAYEE using the taxable income above.

netpayee = 0
personal_relief = 2400
if (taxable_income>0 and taxable_income <= 24000):
    grosspayee = 24000 * 0.1
    netpayee = grosspayee - personal_relief
elif (taxable_income <= 32333) :
    grosspayee = ((taxable_income - 24000) * 0.25) + 2400
    netpayee =grosspayee - personal_relief
elif (taxable_income <= 500000) :
    grosspayee = ((taxable_income - 32333) * 0.30) + 4483.25
    netpayee =grosspayee - personal_relief
elif (taxable_income <= 800000) :
    grosspayee = ( (taxable_income - 500000) * 0.325) + 144783.35
    netpayee = grosspayee - personal_relief
elif (taxable_income > 800000) :
    grosspayee = ((taxable_income - 800000) * 0.35) + 242283.35
    netpayee = grosspayee - personal_relief
else :
    netpayee = 0
    
print("PAYEE: ",round(netpayee))

# Continue with the same program and calculate an individual’s Net Salary using:
# net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

total = nhif + nhdf + nssf + netpayee
net_salary = gross_salary-total
print("NET SALARY: ",net_salary)
