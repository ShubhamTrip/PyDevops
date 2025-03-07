
#For in Loops

for i in range(5):    #Considers i to start from 0.
    print(i)

for i in range(2,5):
    print("The Square value:", i*i)

for i in range(2,10,2):  #Junping by 2
    print("Junp by 2:", i)

for i in range(10,2,-2):  #Jumping by 2 in reverse order
    print("Jumping by 2 in reverse order:", i)

#While loop
i = 0
while i<5:
    print("While loop:", i)
    i += 1

#Break statement
for i in range(10):
    if i == 5:
        break
    print("Break statement:", i)

#Continue statement
for i in range(10):
    if i == 5:
        print("Skipping 5")
        continue
    print("Continue statement:", i)

#Pass statement
# It is used when you want to do nothing
# It is used when you want to keep the loop empty
for i in range(10):
    if i == 5:
        pass
    print("Pass statement:", i)

for i in range(10):
    pass

#Go to statement
# It is not available in python
# It is used to jump to a specific line of code
# It is not recommended to use goto statement

#Printing is a single line
for i in range(10):
    print(i, end = " ")

#Printing in a single line with some separator
for i in range(10):
    print(i, end = ", ")