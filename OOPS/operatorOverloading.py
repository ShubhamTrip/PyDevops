#Operator Overloading #Method Overloading is not possible in Python but can be achieved using None keyword as default values.
#Have ever noticed when we add two int we get sum.
#But, when we add to str we get a concatinated string.

# How this happens?

# Ans- DUNDER functions (__add__, __sub__, __mul__)
#Dunder func allows us to change the way to deal with diff types with operation like + - * etc.

# Something similar is their in string default class(The use of dunder function has changed the way + deals with two strs.)


class ComplexNum:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def showNumber(self):
        print(self.real,"+", self.imaginary, "i")

    def __add__(self, num):
        newReal = self.real + num.real
        newImg = self.imaginary + num.imaginary

        return ComplexNum(newReal, newImg)
    

num1 = ComplexNum(10,3)

num1.showNumber()

num2 = ComplexNum(2,4)

num2.showNumber()


num3 = num1 + num2

num3.showNumber()



#Method overriding is their in python but we just have to reuse func name and no need to add override decorator..

class Parent:
    def show():
        print("hello")

class Child(Parent):
    def show():
        print("hello boy")

# THis is method overriding 