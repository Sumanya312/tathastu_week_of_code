print("enter a list of integers: ",end="")
a = [int(x) for x in input().split()]
size = len(a)

for i in range(size):
    num = a[i]
    left = 1
    right = 1
    for l in range(0,i):
        if a[l]>num:
            right = 0
            break
    for r in range(i+1,size):
        if a[r]<num:
            left = 0
            break
     
    if left == 1 and right ==1:
        print("number found:",num)
        break
