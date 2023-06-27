class Employee:
    company = "Camel"
    salary = 100
    location = "Pathankot"
    @classmethod
    def changeSlary(cls, sal):
        cls.salary=sal

e = Employee()
print(e.salary)
e.changeSlary(455)
print(e.salary)
print(Employee.salary)
