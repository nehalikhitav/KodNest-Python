# Normal Exception
try:
    res = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by Zero")
else:
    print(res)

# Own Exception
x = 10 / 0
raise ZeroDivisionError

age = 15
if age < 18:
    raise ValueError("Age is less than 18: Not Eligible")
else:
    print("Eligible for Vote")
