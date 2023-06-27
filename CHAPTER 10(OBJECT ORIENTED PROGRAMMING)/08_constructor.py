class Employee:
    company ="google"

    def __init__(self, name ,salary, subunit):
        self.name =  name
        self.salary =  salary
        self.subunit =  subunit
        print("Employee is created")

    def getDetails(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of employee is {self.subunit}")

    def getSalary(self,sign):
        print(f"Salryof employee working in {self.company} is {self.salary}\n{sign}")
    
    @staticmethod
    def greet():
        print("Good morning, sir")

harry=Employee("Saurabh","100000", "youtube")
harry.getDetails()