import json

name = input("Enter name:")
marks = int(input("Enter marks: "))

print(name, type(name))
print(marks, type(marks))

person = {"name":name,"marks":marks}
print(person, type(person)) # dictionary

strObj = json.dumps(person)
print(strObj, type(strObj)) # string

#Json.dump() -> dict -> JSON file
with open("person.json", "w") as f:
    json.dump(person,f)


#Json.LOADS() -> JSON string obj to python data
python_data = json.loads(strObj)
print(python_data, python_data["name"], type(python_data))

#json.load() -> JSON file to python data
with open("person.json", "r") as f:
    python_data = json.load(f)
    print(python_data, type(python_data))

#json.dump

import json
students = {
    "name": "Roshan",
    "age" : 23,
    "course": "Python",
    "mobile": 989843920
}
with open("students.json", "w") as f:
    json.dump(students,f)
