
from functools import reduce


#Filter fucntion

nums = {3,2,4,45,46, 64,65, 87}

# def is_even(n):
#     return n%2==0
    
evens = list(filter(lambda n: n%2==0, nums)) #Instead of using a lonf fucntion we use lambda here

#Map function 
#Maps a value to anohter value

double = list(map(lambda n : n*2, evens))

print(double)


#Reduce 

sum = reduce(lambda a,b : a+b ,double)

print(sum)
