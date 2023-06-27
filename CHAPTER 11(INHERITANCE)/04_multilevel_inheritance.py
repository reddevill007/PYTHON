class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing in person....")

class Employee(Person):
    company = "Honda"
    salary = 10000
    def getSalary(self):
        print(f"The salary is {self.salary}")

    def takeBreath(self):
        print("I am luckily breathing in employee")

class Programmer(Employee):
    company = "fivver"
    def takeBreath(self):
        print("I am luckily breathing in programmer")

    def getSalary(self):
        print("no salry to programmer")

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()
print(pr.country)
pr.takeBreath()