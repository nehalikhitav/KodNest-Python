list1 = [1,2,3,4,5]
l = 0
r = len(list1)-1
while l<r:
    list1[l],list1[r]=list1[r],list1[l]
    l+=1
    r-=1
print(list1)

list2 = [1,2,3,4,5]
l = []
for i in range(len(list2)-1,-1,-1):
    l.append(list2[i])
print(l)

list3 = [1,2,3,4,5]
l = []
for i in list3:
    l.insert(0,i)
print(l)