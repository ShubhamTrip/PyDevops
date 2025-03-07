# boy = 10

# print("The value of boy is", boy , "Hello")

# x= 10
# y = 22.5435345345
# z = "Hello"
# a = True
# b = 2+3j

# print(type(b), type(y), type(z), type(a), type(x))

# print("The value of y is", y)

# # String formating

# # 1. Formating using % operator
# print("The value of y is %.2f" %y)

# #2. Formating using format method {}

# print("The value of y is {:.2f}".format(y))

# print("The value of integer is {} and string is {}".format(x,z))

# print("The value of integer is {1} and string is {0}".format(z,x))

# # User Input

# name = input("Enter your name: ")

# print("Your naame is", name)

# print("You can enter here as well", input())

# # User input of specific type

# # The default type of input is string
# # If you want to take input of specific
# # type then you can typecast the input

# count = int(input("Enter the count: "))
# print("The count is", count)

# # Multiple input in one line

# a,b,c = input("Enter three values: ").split()
# print("The values are", a,b,c)

# # Typecasting the input
# a,b,c = map(int, input("Enter three values: ").split())
# print("The values are", a,b,c)

# #Since python is dynamically typed language so the variable can be reassigned
# # to any type of value
# # age = 10
# # age = "Hello"

# # print(age)


# # String Operations

# # 1. Concatenation
# a = "Hello"
# b = "World"
# print(a+b)

# #Formatting
# name = "John"
# age = 20

# statment = f"My name is {name} and I am {age} years old"
# print(statment)

# st2 = "My name is {} and I am {} years old".format(name, age)
# print(st2)

# print(f"The name is {name} and the age is {age}")

# # String Slicing
name = "Hello World"
print(name[0])
print(name[0:5]) # 0 to 4 as 5 is exclusive
print(name[6:]) # 6 to end
print(name[:5]) # 0 to 4
print(name[-1]) # Last character

new_name = name[:5] + name[6:]
print(new_name)

