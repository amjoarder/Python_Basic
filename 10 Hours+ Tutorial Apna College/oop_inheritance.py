class car:
    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Break")

class ToyotaCar(car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Land Cruiser")
print(car1.start())

'''
# Multiple Inheritance
class newCar(car, ToyotaCar):

'''
