def my_function():
  print("Hello from a function")

my_function()

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function,
#add a * before the parameter name in the function definition.

def myFunc1(* arguments):
  print(arguments[0])
#  print(arguments[2]) #Calling values that doesnt exists throws error

myFunc1("Hello")

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Positional-Only Arguments
#If you wish to make take args strictly in positional format not in keywords 

def my_function(x, /): # Have to place / at last
  print(x)

# my_function(x = 3) This shows error

my_function(3)

#Keywords only

def my_function(*, x):
  print(x)

my_function(x = 3)

#combination

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)