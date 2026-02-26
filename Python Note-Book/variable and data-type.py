# Variables — no type declaration needed
name = "Ali" # str (string)
age = 20 # int (integer)
height = 5.9 # float (decimal)
is_pass = True # bool (True/False)
data = None # NoneType (empty)
# Check type
print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_pass)) # <class 'bool'>
# Multiple assignment
x = y = z = 0
a, b, c = 10, 20, 30
print(a, b, c) # 10 20 30
# Swap variables
a, b = b, a
print(a, b) # 20 10
