#Inheriting Parent Porperites in child
#There are three types of Inheritance ---. 1. Single 2. Multiple 3. Multi Level

class Car:
    country = "India"

    @staticmethod #Used to define static methods
    def startCar():
        print("Droom....")

#How to change Class level Attributes using a methods of class.
# Class attr cannot be changeed using normal methods where we use self because it will set prop for obj
#So There are three ways
#1  # def changeCountry(*,country):
    #     Car.country = country

#2 using __class__ prop of self to access and modify clas level attrs.
    
    # def changeCountry(self, name):
    #     self.__class__.country = name

#3 Using classmethod decorator
# These are used to change class prop without touching or using obj level methods
    @classmethod 
    def changeClassAttr(cls,*,name):  #Class methods use first arg as referance to class
       cls.country = name

class Toyota(Car):
    def __init__(self, year, type):
        super().__init__()
        self.carType = type
        self.year = year

    def getInfoToyota(self):
        print(f"Year of Menu is {self.year} and type is {self.carType}")


#This is multilevel inheritance
class Scorpio(Toyota):
    def __init__(self, *,color, price, type, year):
        super().__init__(year, type)
        self.color = color 
        self.price = price
        self.whatIsPrice = f"The price is {self.price}" # But this doesnt reflect cahnge if we change price now.
        #Whats the solution?
        #Either we use a method to reflect price which we dont want to do.
        #2nd option is to use @property --> Using this a function can be as a attribute of variable to acces property
    
    @property
    def newPrice(self):
        return f"The new price is {self.price}"



#Now suppose we wish to create obj of Scoprio and check its year of Manufacturing
#We cant do this if we have not set this prop in Scorpio class since it will be empty..

#So to set prop of parent class from child class we have to use super() function. inside init to call init of parent class.

s1 = Scorpio(color = "red", price = 200000, type = "SUV", year= "2020")

print(s1.getInfoToyota())

s1.price = 30000

print(s1.newPrice) # If a function but works as property of variable


print(Car.startCar()) # Can be directly used.

c1 = Car()

print(c1.startCar()) # Can be accessed by objs

#c1.changeCountry("Tasmania")

Car.changeClassAttr(name = "Australia") 

print(Car.country)



    