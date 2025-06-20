# There is  20 ways to check the data Types

# 1. Type()  ,  type(a)  , Most basic and official way to find the data types

a="hello world"

print(type(a))

# 2.  isinstance()  ,  ininstance(a , int) , Check if variable is of a specific type

a = "hello world" 

print(isinstance(a, int))

# 3. __class__ , a.__class__  , Returns the class object of the variable

a = 44.22

print(a.__class__)

# 4.  __class__.__name__ ,  a.__class__.__name__  ,  Gives the type name as a clean string