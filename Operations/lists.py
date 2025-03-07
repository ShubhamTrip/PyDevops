
#List 

list1 = [1,2,3,4,5]

print(list1)
print(list1[-1])

length = len(list1)
print(length)

# Lists are mutable
list1[0] = 10
print(list1)

# Some Properties of List
# List are mutable
# List are ordered
# List can have duplicate values
# List can have different data types

#Operations on List

# 1. Append
list2 = [1,2,3,4,5]
list2.append(6)
print(list2)

# 2. Insert
list2.insert(2, 10)
print(list2)

list2.insert(-2, 20) 
print(list2)
# Output: [1, 2, 10, 3, 4, 20, 5, 6]
# Why at 3 last position?
# Because VALUE is inserted and the previous value is shifted to the right
#Also 7 - 2 = 5, so 20 is inserted at 5th position

# 3. Extend
list2.extend([7,8,9])
print(list2)
# Since append takes only one argument so if you want to append multiple values then you can use extend

# 4. Remove
list2.remove(20)
print(list2)
# Removes the first occurence of the value

# 5. Pop
list2.pop()
print(list2)
# Removes the last element of the list

list2.pop(2)
print(list2)
# Removes the element at the given index

# 6. Clear
list2.clear()
print(list2)
# Removes all the elements of the list

#7. del
list2 = [1,2,3,4,5]
del list2[2]
print(list2)
# Removes the element at the given index
