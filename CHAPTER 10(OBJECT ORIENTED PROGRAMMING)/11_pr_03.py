class Sample:
    a="Saurabh"

obj = Sample()
obj.a="Shivam"

print(Sample.a)  # Sample.a will print orignal value of a inside the Sample class
print(obj.a)     # obj.a will print updated value of a of the object