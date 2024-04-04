class Circle:
    def __init__(self,rad):
        self.rad=rad
    
    def area(self):
        return (22/7)*self.rad**2
    def perimeter(self):
        return 2*(22/7)*self.rad 

c1=Circle(4)
print(c1.area())
print(c1.perimeter())


