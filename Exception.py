#index err
skills = ["Python","Sql","DSA"]
try:
   print(skills[3])
except IndexError:
    print("Index out of range")
    
print("End of program")

#zerodivisionError
a = 10
b = 0
try: 
    print(a/b)
except ZeroDivisionError as e:
    print(f"Cannot divide by zero {e}")
    
print("End of program")

#typererror
try:
    age=int(input("Enter your age"))
    print("Your age is", age)
except ValueError as e:
    print("Invalid age",e)
print("End of program")


#keyerror
student ={
    "Name":"Nehal",
    "Age":20,
    "Course":"Java"
}
try:
    print(student["Grade"])
except KeyError as e:
    print(f"Invalid key {e}")
    
print("End of program")
