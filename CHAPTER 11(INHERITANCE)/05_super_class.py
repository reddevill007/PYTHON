class Person:
    country = "India"
    def __init__(self):
        print("Initializing a Person......\n")
    def takeBreath(self):
        print("I am breathing in person....")

class Employee(Person):
    company = "Honda"
    salary = 10000

    def __init__(self):
        super().__init__()
        print("Initializing a Employee......\n")

    def getSalary(self):
        print(f"The salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am luckily breathing in employee")

class Programmer(Employee):
    company = "fivver"
    def __init__(self):
        super().__init__()
        print("Initializing a Programmer......\n")

    def takeBreath(self):
        super().takeBreath()
        print("I am luckily breathing in programmer")

    def getSalary(self):
        print("no salry to programmer")

p = Person()
# p.takeBreath()

e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()