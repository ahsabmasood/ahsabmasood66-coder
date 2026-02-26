# Basic input — always returns a string
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))
# print() with sep and end
print("Name:", name, "Age:", age)
print("A", "B", "C", sep="-") # A-B-C
print("Hello", end=" ")
print("World") # Hello World
# f-strings (best way — Python 3.6+)
print(f"Name: {name}, Age: {age}, GPA: {gpa:.2f}")
# .format() method
print("Name: {}, Age: {}".format(name, age))
print("GPA: {:.2f}".format(gpa))
# % formatting (old style)
print("Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa))
# Multiline print
print("""
Student Report
--------------
Name : Ali
Age : 20
GPA : 3.85
""")