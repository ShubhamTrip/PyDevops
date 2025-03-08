# Exception Handling is used to handle runtime error. Where we dont want to program to crash.

a=5
b=0

try:
    print("Resource Open") #Now we havve to close it Eg we have to close dbconnections.
    print(a/b)
#   print("Close Resource") If you close it here now as print(a/b) throws error so it will not be executed


# except Exception as e:
#     print("Hey you cannot devide number by zero")

except ZeroDivisionError as e:
    print("Hey you cannot devide number by zero", e) 
#   print("Close Resource") If here may be is try has everything right it will be get into expect

finally:  #We close or do things that are to be done for sure here in finally
    print("Resource Closed")
