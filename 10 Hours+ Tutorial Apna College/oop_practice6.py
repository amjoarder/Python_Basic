class Order:
    def __init__(self, item, price):
        self.item =item
        self.price = price

    def __gt__(self,O2):
        return self.price>O2.price


O1 = Order("Chocolate",1300)
O2 = Order("Rice",900)

print(O1<O2)