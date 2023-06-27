class Programmer():
    company = "Microsoft"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Programmer is created")
  
    def getDetails(self):
        print(f"The name of the company of the employee is {self.company}")
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The language of employee is {self.language}\n")


saurabh = Programmer("Saurabh", "20k", "c language")
saurabh.getDetails()

shivam = Programmer("Shivam", "200k", "c++ language")
shivam.getDetails()

Shilpy = Programmer("Shilpy", "50k", "python language")
Shilpy.getDetails()

Rahul = Programmer("Rahul", "10k", "java language")
Rahul.getDetails()
