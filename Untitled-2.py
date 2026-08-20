class Car(): 
    color = "red"
    @staticmethod
    def  start():
        print("car is starting...")

    @staticmethod
    def stop():
        print("car is stopping...")  

class tayotaCar(Car):
    def __init__(self, brand):
        self.brand = brand 

class fortuner(tayotaCar): 
        def __init__(self, type):
             
            self.type = type 



car1 = fortuner("petrol")
print(car1.type) 
print(car1.start())

# car1 = tayotaCar("fortuner")
# car2 = tayotaCar("innova")
# print(car1.name)
# print(car2.name)
# print(car1.start())  
# print(car1.color)
