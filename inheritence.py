class Car(): 
    color = "red"
    @staticmethod
    def  start():
        print("car is starting...")

    @staticmethod
    def stop():
        print("car is stopping...")  

class tayotaCar(Car):
    def __init__(self, name):
        self.name = name 


car1 = tayotaCar("fortuner")
car2 = tayotaCar("innova")
print(car1.name)
print(car2.name)
print(car1.start())  
print(car1.color)
