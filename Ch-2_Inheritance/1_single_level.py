class company:
    title:str = "consultancy"

    def __init__(self, company_name:str):
        self.company_name = company_name
    
    def info(self):
        return f"company name is {self.company_name}"
    
class employee(company):

    def __init__(self,employee_name:str, company_name:str):
        self.employee_name = employee_name
        self.company_name = company_name

    def employee_info(self):
        response = company.info(self)
        print(f"The employee : {self.employee_name}, {response} ")

employee_obj = employee("Chetan", "ZS")

employee_obj.employee_info()
    
        