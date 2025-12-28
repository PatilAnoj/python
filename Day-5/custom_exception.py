class SalaryNotInRange(Exception):
    def __init__(self,salary,message="Salary not in range 5000-15000"):
        self.salary=salary
        super().__init__(message)

def validate_salary(salary):
    if salary <5000 or salary>15000:
        raise SalaryNotInRange(salary)
    
try:
    validate_salary(4000)
except SalaryNotInRange as e:
    print(e)