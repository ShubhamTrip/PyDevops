
# #TUPLE

# tuple1 = (1,2,3,4,5)

# print(tuple1)
# print(tuple1[-1])

# length = len(tuple1)
# print(length)

# # Tuples are immutable
# # tuple1[0] = 10
# # print(tuple1)
# # This wi;; throw error

# # Some Properties of Tuple
# # Immutable
# # Tuples are ordered
# # Tuples can have duplicate values
# # Tuples can have different data types

# #Operations on List

# #To change value inside tuple you have to copy tuple to list and after change you have to convert it back.
# tup2 = [1,2,3,4,5]

# list = list(tup2)

# list.append(6)

# tup2 = tuple(list)

# print(tup2)


# # You can delete a tuple as a whole
# del tup2

# #Unpacking Tuple
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# #If the number of variables is less than the number of values, 
# # you can add an * to the variable name and the values will be assigned to the variable as a list:

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, *yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


#Dictionary

diction = {
    "name" : "Shubham",
    "age" : 25
}

#Repeation of key is not allowed

#constructor func dict()

dict2 = dict(name = "Radha", age =  24)

#Access 

print(diction["name"])

print(diction.get("name"))

# Works same

# Adding value

diction.update({"year" : 2025, "name" : "Ramu"}) # Adding and updating old value.

print(diction)

diction["roll"] = "Developer"

print(diction)




