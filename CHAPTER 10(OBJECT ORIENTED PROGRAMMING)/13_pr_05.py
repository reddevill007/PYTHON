class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print(f"The name of tarin: {self.name}")
        print(f"The seats available in this tarin: {self.seats}")

    def fareInfo(self):
        print(f"The price of ticket: Rs{self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! \nYour seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            ("Sorry the Train is full please try in tatkal")

intercity=Train("Intercity Express: 14345", 90 , 300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()

