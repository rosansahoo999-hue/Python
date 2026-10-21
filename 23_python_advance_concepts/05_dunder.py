class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = Employee("Rosan", 45999)
print(e.name, e.salary)