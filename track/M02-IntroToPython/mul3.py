limit = int(input())
target = int(input())

count = 0
total = 0
found = False

# Examine every number from 1 to the limit
for i in range(1,limit):
    #if i == target:
        # found = True
    if i%3 == 0:
        count+=1
        total +=i
        if i == target:
            found = True
# Display the count, total and search result
print(f"Count: {count}")
print(f"Sum: {total}")
if found == True:
    print("Target Found: Yes")
else:
    print("Target Found: No")

