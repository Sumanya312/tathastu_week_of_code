res=[]
def sum(l,s=0):
    for i in l:
        res.append(s+i)
        l1=list(l)
        l1.remove(i)
        sum(l1,s+i)

print("enter elements of list: ")
l = [int(x) for x in input().split()]
n = min(l)
sum(l)
sumList = list(set(res))

while 1:
    if n not in sumList:
        print("the least integer is: ", n)
        break
    n +=1
