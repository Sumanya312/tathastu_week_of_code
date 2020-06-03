print("enter space generated integers: ")
l = [int(x) for x in input().split()]

size = len(l)
max = l[-1]
l1=[0]*size
for i in range(size-2,-1,-1):
    l1[i]=max
    if l[i]>max:
        max=l[i]

print("the new list is: ",l1)
