class Employee:
    company ="google"
    def getSalary(self):
        print(f"Salryof employee working in {self.company} is {self.salary}")

harry=Employee()
harry.salary = 10000000
harry.getSalary()
Employee.getSalary(harry)#the above syntax is converted into this with the help of self
