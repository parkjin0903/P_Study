#class

class Car: 
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value

#instance

myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "blue"
myCar2.speed = 0

#field, method

myCar1.upSpeed(30)
print("color of car is %s and current speed of the car is %d." %(myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("color of car is %s and current speed of the car is %d." %(myCar2.color, myCar2.speed))