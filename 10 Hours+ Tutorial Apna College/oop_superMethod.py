class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Break")


class ToyotaCar(car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = ToyotaCar("Land Cruiser", "SUV")
print(car1.type)

