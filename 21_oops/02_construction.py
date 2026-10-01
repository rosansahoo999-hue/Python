class Employee:
    company = 'HP'

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self): 
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} Years")

e1 = Employee(35000, 'Jhon Deo', 4)
# print(e1.get_salary())
e1.get_info()
