class complex:
    def __init__(self, real, img):
        self.real = real
        self.img=img
    def showNum(self):
        print(self.real,"i+",self.img,"j" )

#dunder function __something__
    def __add__(self, num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complex(newReal, newImg)

num1=complex(1,3)
num1.showNum()

num2=complex(1,4)
num1.showNum()

'''num3=num1.add(num2)
num3.showNum()

#using dunder function we can do it better
'''

num3=num1+num2
num3.showNum()