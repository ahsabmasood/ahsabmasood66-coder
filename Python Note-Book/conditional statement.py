# if / elif / else
score = 73
if score >= 90:
 print("Grade: A+")
elif score >= 80:
 print("Grade: A")
elif score >= 70:
 print("Grade: B")
elif score >= 60:
 print("Grade: C")
elif score >= 50:
 print("Grade: D")
else:
 print("Grade: F")
# Output: Grade: B
# Ternary operator (one-line if-else)
status = "Pass" if score >= 50 else "Fail"
# Nested if
age = 25
income = 50000
if age >= 18:
    if income >= 30000:
        print("Eligible for loan")
    else:
        print("Income too low")
else:
    print("Too young")
# Match statement (Python 3.10+)
day = "Monday"
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Unknown")
