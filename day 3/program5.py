print("enter a list: ")
l1 = [x for x in input().split()]
print("enter second list: ")
l2 = [x for x in input().split()]

l3 = []
l3.extend(l1)

for i in l2:
    if i not in l1:
        l3.append(i)

print(l3)
