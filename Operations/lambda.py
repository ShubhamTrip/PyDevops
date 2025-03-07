
#Lambdas are inline function
a = lambda x, n : n * x

print(a(3,5))

b = lambda x, y : x if x>y else y
print(b(2,3))

c = lambda x, y : x if x>y else ( "Both are equal" if x ==y else y )

print(c(2,2))

result = lambda x,y : f"{x} is smaller than {y}" \
if x < y else (f"{x} is greater than {y}" if x > y \
               else f"{x} is equal to {y}")

#Use \ if you wish to change line. But remember no space is allowed after \

# print for numbers
print(result(12, 11))
print(result(12, 12))
print(result(12, 13))