# Write a program that takes input of someone's basic salary and benefits,
# adds them to find the gross salary then uses  the gross salary to find the NHIF

s = float(input("Enter basic salary: "))
b = float(input("Enter benefits: "))
 
def find_gross_salary(basic_salary,benefits):
    gross_salary = basic_salary + benefits
    return gross_salary

total_gross = find_gross_salary(s,b)
print("gross:",total_gross)



def find_nhif(gross_salary):
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
    return nhif

total_nhif = find_nhif(total_gross)
           
print("NHIF: ",total_nhif)



# # Continue with the program above, then use  the gross salary to find the NSSF. 
# # To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary.
# # BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

def find_nssf(gross_salary,rate=0.06):
    nssf = 0
    if (gross_salary > 0 and gross_salary <= 18000) :
        nssf = (gross_salary * rate)
    else :
        nssf = 18000 * rate
    return nssf
    
total_nssf = find_nssf(total_gross,rate=0.06)
print("NSSF: ",total_nssf)


# # Continue with the same program and calculate an individual’s NHDF using:i.e NHDF = gross_salary *  0.015
def find_nhdf(gross_salary,amount=0.015):
  nhdf = 0
  if(gross_salary <= 83333):
    nhdf = gross_salary * amount
  else :
    nhdf =2500
  return nhdf

total_nhdf = find_nhdf(total_gross,amount=0.015)
print("NHDF: ",total_nhdf)

# # nssf +nhdf

# # Calculate the taxable income.i.e taxable_income = gross salary - (NSSF + NHDF) 
def find_taxable_income(gross_salary,nssf,nhdf):
    taxable_income = gross_salary-(nssf+nhdf)
    return taxable_income

total_taxableincome = find_taxable_income(total_gross,total_nssf,total_nhdf)
print("TAXABLE INCOME: ",total_taxableincome)



# # Continue with the same program and find the person's PAYEE using the taxable income above.

def find_payee(taxable_income,personal_relief=2400):
    netpayee = 0
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
    return netpayee

total_payee = find_payee(total_taxableincome,personal_relief=2400)
print("PAYEE: ",round(total_payee))

# # Continue with the same program and calculate an individual’s Net Salary using:

def find_net_salary(gross_salary,nhif,nhdf,nssf,netpayee):
    total = nhif + nhdf + nssf + netpayee
    net_salary = gross_salary-total
    return net_salary

total_netsalary = find_net_salary(total_gross,total_nhif,total_nhdf,total_nssf,total_payee)
print("NET SALARY: ",total_netsalary)
