class Employee:
    company ="google"
    def getSalary(self,sign):
        print(f"Salryof employee working in {self.company} is {self.salary}\n{sign}")
        
    @staticmethod
    def greet():
        print("Good morning, sir")

harry=Employee()
harry.salary = 10000000
harry.getSalary("Thnks") #indicate to the sign
harry.greet()