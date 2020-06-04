print("enter a list of integers: ")
l = [int(x) for x in input().split()]

l.sort()

num = 1

x=0

for i in range(len(l)):
    if l[i]==1:
        x=i
        break

if x==0:
    print("the smallest positive integer missing: ",1)
else:
    for i in range(x,len(l)):
        if num==l[i]:
            num+=1
        elif l[i]>num:
            break
    print("the smallest positive integer missing:",num)
