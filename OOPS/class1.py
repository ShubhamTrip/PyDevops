
# Init is a special func provided by python. It is constructor.
# Any func starting from and ending with __ is a special constructor..
# We dont need to declaring variable since python allows dynamic typing(Dec and init happening together). 
# Imagine declaring var without value which is not possible..
# Object Variable  are declared and init inside init functions and can be accessed with the help of slef.
# Class variables are declared inside class and can be accessed by using dot operator.
# self is this of 3g Langs.
class Book:
    publication = "Vidhya Bharati" # Can be directly accessed using . oprator.
    
    author = "Shubham" #We generally dont do this.

    def __init__(self,title, author, price, quantity):

        #Initialization and declaration is happening here..
        self.title = title
        self.author = author # Here the class attribute is automatically overwritten and has become obj attribute.
    
        self.price = price
        self.quantity = quantity
        self.__discount = price * 0.10 # This is private now
    
    def getInfo(self):
        print(f"{self.title} is a great book.")

    def getDisPrice(self):
        print("Discount is here")
        return self.__discount
    
    def changeBookName(self, *, newName):
        self.title = newName


#If you print(book1) without defining __str__ or __repr__ it show <__main__.Book object at 0x101299a90>.
#To show some relevent info we can use these func

    def __str__(self):  # Same as __repr__ function but repr is for debugging and str is for user readablitiy.
        return f"Price is {self.price} and title is {self.title}"

book1 = Book("Good Habits", "Shubbh", 300, 50)

print(Book.publication)

print(book1)

book1.getInfo()

discount = book1.getDisPrice()

print(f"The discount is {discount}")

book1.changeBookName(newName="Your good Habbits")

print(book1)

del book1 # This is used to delete an object.
