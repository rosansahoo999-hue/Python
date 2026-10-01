# class: class is a blueprint or a template. Eg. form for an exam that contains name, age, elective, father's name etc.

# object: specific instance created from the template (class). Eg. Form which contains the data for John Doe.

class Employee:
    company = 'HP'

    def get_salary(self): # self is important here because self is a way to reference the object of the class which is beings created.
        print(self)
        return 35000

e = Employee()   # An object of class employee is created here.
print(e.get_salary())  # employee is get salary method is called.
print(e.company)
