# Create a class called Payroll whose major task is to calculate an individual’s Net Salary
#  by getting the inputs basic salary and benefits. Create 5 different class methods which will calculate the payee, 
#  nhif_deductions, nhdf_deductions, nssf_deductions, gross_salary and net_salary. 

class Payroll():


    def __init__(self,s,b):
        self.basic_salary=s
        self.benefits=b
        self.find_gross_salary()
        self.find_nhif()
        self.find_nssf()
        self.find_nhdf()
        self.find_taxable_income()
        self.find_payee()
        self.find_net_salary()
        # self.add()


    def find_gross_salary(self):
        self.gross_salary= self.basic_salary + self.benefits
        print("gross salary: ",self.gross_salary)

    def find_nhif(self):
        
        if (self.gross_salary <= 5999) :
            self.nhif = 150

        elif (self.gross_salary >= 6000 and self.gross_salary <= 7999) :
            self.nhif = 300

        elif (self.gross_salary >= 8000 and self.gross_salary <= 11999) :
            self.nhif = 400
        elif (self.gross_salary >= 12000 and self.gross_salary <= 14999) :
            self.nhif = 500

        elif (self.gross_salary >= 15000 and self.gross_salary <= 19999) :
            self.nhif= 600

        elif (self.gross_salary >= 20000 and self.gross_salary <= 24999) :
            self.nhif = 750

        elif (self.gross_salary >= 25000 and self.gross_salary <= 29999):
            self.nhif = 850

        elif (self.gross_salary >= 30000 and self.gross_salary <= 34999) :
            self.nhif = 900

        elif (self.gross_salary >= 35000 and self.gross_salary <= 39999) :
            self.nhif = 950

        elif (self.gross_salary >= 40000 and self.gross_salary <= 44999) :
            self.nhif = 1000

        elif (self.gross_salary >= 45000 and self.gross_salary <= 49999) :
            self.nhif = 1100

        elif (self.gross_salary >= 50000 and self.gross_salary <= 59999) :
            self.nhif = 1200

        elif (self.gross_salary >= 60000 and self.gross_salary <= 69999) :
            self.nhif = 1300

        elif (self.gross_salary >= 70000 and self.gross_salary <= 79999) :
            self.nhif = 1400

        elif (self.gross_salary >= 80000 and self.gross_salary <= 89999) :
            self.nhif = 1500

        elif (self.gross_salary >= 90000 and self.gross_salary <= 99999) :
            self.nhif = 1600

        else :
           self.nhif = 1700
        
        print("NHIF: ",self.nhif)

    def find_nssf(self,rate=0.06):
        # rate = 0.06
        if (self.gross_salary > 0 and self.gross_salary <= 18000) :
            self.nssf = (self.gross_salary * rate)
        else :
            self.nssf = 18000 * rate
        print("NSSF: ",self.nssf)
   
    def find_nhdf(self,amount=0.015):

        if(self.gross_salary <= 83333):
          self.nhdf = self.gross_salary * amount
        else :
          self.nhdf =2500
        print("NHDF: ",self.nhdf)

    def find_taxable_income(self):
        # self.nssf=nssf
        # self.nhdf=nhdf
        self.taxable_income = self.gross_salary-(self.nssf+self.nhdf)
        print("TAXABLE_INCOME: ",self.taxable_income)
    
    def find_payee(self,personal_relief=2400):
        if (self.taxable_income>0 and self.taxable_income <= 24000):
           grosspayee = 24000 * 0.1
           self.netpayee = grosspayee - personal_relief
        elif (self.taxable_income <= 32333) :
           grosspayee = ((self.taxable_income - 24000) * 0.25) + 2400
           self.netpayee =grosspayee - personal_relief
        elif (self.taxable_income <= 500000) :
           grosspayee = ((self.taxable_income - 32333) * 0.30) + 4483.25
           self.netpayee =grosspayee - personal_relief
        elif (self.taxable_income <= 800000) :
           grosspayee = ( (self.taxable_income - 500000) * 0.325) + 144783.35
           self.netpayee = grosspayee - personal_relief
        elif (self.taxable_income > 800000) :
           grosspayee = ((self.taxable_income - 800000) * 0.35) + 242283.35
           self.netpayee = grosspayee - personal_relief
        else :
           self.netpayee = 0
        netpayee = round(self.netpayee)
        print("NETPAYEE: ",netpayee)

    def find_net_salary(self):
        self.total = self.nhif + self.nhdf + self.nssf + self.netpayee
        self.net_salary = self.gross_salary-self.total
        print("NET SALARY: ",self.net_salary)

    

calc_gross_salary = Payroll(float(input("Enter gross salary: ")),
                     float(input("Enter benefits: "))
                    )


