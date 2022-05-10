#class

class Car: 
    color = "" #instance variable
    speed = 0 #instance variable
    count = 0 #class variable
    
    def __init__(self):
        self.color = "red"
        self.speed = 0
        Car.count += 1


myCar1, myCar2 = None, None

myCar1 = Car()
myCar1.speed = 30

myCar2 = Car()
myCar2.speed = 60