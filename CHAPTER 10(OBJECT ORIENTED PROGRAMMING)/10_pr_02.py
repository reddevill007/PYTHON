import math


class Calculator:

    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

    def squareroot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")


n=int(input("Enter the number: "))
a=Calculator(n)
a.square()
a.cube()
a.squareroot()