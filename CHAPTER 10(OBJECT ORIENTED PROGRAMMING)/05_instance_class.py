class Employee:
    company="Google"
    salary=100

saurabh=Employee()
shivam=Employee()

# creating instance attribute for both object
saurabh.salary=300
shivam.salary=400
print(saurabh.salary)
print(shivam.salary)

#below line throws an error as address is not present in instance/class
#print(shivam.address)