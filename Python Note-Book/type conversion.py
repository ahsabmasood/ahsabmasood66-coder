# Implicit conversion (Python does automatically)
result = 10 + 3.5 # int + float = float
print(result) # 13.5
print(type(result)) # <class 'float'>
# Explicit conversion (type casting)
x = int("42") # string -> int
y = float("3.14") # string -> float
z = str(100) # int -> string
b = bool(0) # int -> bool (0=False, else True)
n = int(True) # bool -> int (True=1, False=0)
print(x, y, z, b, n) # 42 3.14 100 False 1
# int() truncates floats
print(int(9.99)) # 9 (does NOT round)
# Common errors
# int("hello") -> ValueError
# int(None) -> TypeError