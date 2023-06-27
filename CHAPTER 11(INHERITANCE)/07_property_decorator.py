class Employee:
    company = "Indian Oil"
    salary = 5000
    salarybonous = 500

    @property
    def totalSalary(self):
        return self.salary + self.salarybonous

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonous = val-self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5600
print(e.salary)
print(e.salarybonous)
