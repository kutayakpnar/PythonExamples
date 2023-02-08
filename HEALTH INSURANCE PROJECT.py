class HealthInsurance():
    def __init__(self,companyname,foundationyear,foundername,companyslogan,num_of_employees,num_of_clients):
        self.companyname=companyname
        self.foundationyear=foundationyear
        self.foundername=foundername
        self.companyslogan=companyslogan
        self.num_of_employess=num_of_employees
        self.num_of_clients=num_of_clients

    def printreport(self):
        print(f"""
        Company Name:{self.companyname} was founded in {self.foundationyear}.
        The founder of the company is {self.foundername}.
        The company slogan is {self.companyslogan}
        Number of Employess :{self.num_of_employess}
        Number of Clients:{self.num_of_clients}""")

    def sup_health_insurance(self,age,chronic_disase,income):
        if age>=60 and chronic_disase==True and income<6000:
            print("We are sorry.You are not eligible for supplemental health insurance.")
        elif age <= 60 and chronic_disase==False and income>6000:
            print("Congratulations! You can get supplemental health insurance!")

    def uptadeclientnumber(self,number):
        self.num_of_clients+=number
        print(f"New Number of Client:{self.num_of_clients}")

company1=HealthInsurance("Healthy",2012,"Bob Mayer","We care for you.",3500,13230)
company1.printreport()
company1.uptadeclientnumber(780)
company1.printreport()
