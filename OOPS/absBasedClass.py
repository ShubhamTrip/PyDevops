#Since Abstract Classes are not present in python we use abc module(Abstract based Class Module).

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):  # Implements abstract class
    #Now if we dont define process method it will throw an error..

    def process(self):
        print("Hello Laptop")


l1 = Laptop()

l1.process()


# Use of Abstract Classes

#It is useful while designing applications, we have to follow a standard way of making a class.

#For example If we have a Computer abstract class. So when ever we have to create a Laptop or Tablet or anyother class that implements Computer 

# It will become mandatory to implement certain method predefine in the abstract class.


# We can Under Interfaces using Zope module..