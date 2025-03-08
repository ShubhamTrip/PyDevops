# #Iterator

# nums = [1,2,3,4,5,6,7,8]


# it = iter(nums)

# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# print(next(it))


# #Our own Iterator
# class TopTen:
#     def __init__(self):
#         self.num =1
    
#     def __next__(self):

#         if self.num <= 10:
#             val = self.num
#             self.num += 1
#             return val
#         else: 
#             raise StopIteration
    
# val = TopTen()


# print(next(val))
# print(next(val))
# print(next(val))



#Generator 

def topten():

    yield(5) # returns a iterator 
    yield(4)
    yield(2)
    yield(1)
    yield(0)
    


value = topten()

print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))


# . Or 

for i in value:
    print("Value: ", i)