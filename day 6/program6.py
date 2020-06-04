print("enter a list of integers: ",end="")
l = [int(x) for x in input().split()]

size = len(l)
x = -1
flag=0

for i in range(1,size):
    if l[i-1]>l[i]:
        x=i
        break


if x!=-1:
    if x==size-1:
        if l[size-1]<l[0]:
            print("the numbers are sorted and rotated")
        else:
            print("the numbers are not sorted and rotated")
    else:
        for i in range(x,size-1):
            if l[i+1]<l[i]:
                flag=1
                break
        if flag==0:
            if l[size-1]<l[0]:
                print("the numbers are sorted and rotated")
            else:
                print("the numbers are not sorted and rotated")
        else:
            print("the numbers are not sorted and rotated")
else:
    print("the numbers are not sorted and rotated")
