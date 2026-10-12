file = open("demo.txt",'r')
print(file.read())
file.close()

file = open("demo.txt","w")
file.write("PYTHON IS FUN")
file.close()

file = open("demo.txt","r")
print(file.read())#Entire file
print(file.readline())#readline
print(file.readlines())# all lines in list)

# without closing we can use with keyword
with open("demo.txt",'r') as file:
    print(file.read())
    print(file.closed)
print(file.closed)

with open("demo.txt","a") as file:
    file.write("hello developer")
    print(file.closed)
print(file.closed)

f = open("demo.txt","a")
f.write("hello")
f.close()