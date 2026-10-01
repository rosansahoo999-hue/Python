
class Employee:
    company = 'Asus'  # This is class attributes.

    def __init__(self, salary, name, bond, company):  
        self.salary = salary  # create instance attributes name, salary and assign with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self): 
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} Years")

e = Employee(3400, 'Jhon', 3, 'Tesla')
print(e.company) # will always print instance attributes whenever presents.
print(Employee.company) # This will always prints the class attributes.

# Object introspection
print(dir(e))