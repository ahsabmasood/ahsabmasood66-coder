# ■■ Arithmetic Operators ■■
a, b = 17, 5
print(a + b) # 22 Addition
print(a - b) # 12 Subtraction
print(a * b) # 85 Multiplication
print(a / b) # 3.4 True division
print(a // b) # 3 Floor division
print(a % b) # 2 Modulus (remainder)
print(a ** b) # 1419857 Power
# ■■ Comparison Operators ■■
print(a > b) # True
print(a < b) # False
print(a == b) # False
print(a != b) # True
print(a >= 17) # True
# ■■ Logical Operators ■■
x, y = True, False
print(x and y) # False (both must be True)
print(x or y) # True (at least one True)
print(not x) # False
# ■■ Bitwise Operators ■■
print(5 & 3) # 1 AND
print(5 | 3) # 7 OR
print(5 ^ 3) # 6 XOR
print(~5) # -6 NOT
print(5 << 1) # 10 Left shift
print(5 >> 1) # 2 Right shift
# ■■ Assignment Operators ■■
n = 10
n += 5 # n = 15
n -= 3 # n = 12
n *= 2 # n = 24
n //= 5 # n = 4
n **= 3 # n = 64
print(n) # 64
# ■■ Identity and Membership ■■
lst = [1, 2, 3]
print(3 in lst) # True
print(5 not in lst) # True
a = [1, 2]
b = a
print(a is b) # True (same object)
print(a is [1, 2]) # False (different object)