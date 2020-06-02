print("enter elements of a tuple: ")
t = (int(x) for x in input().split())

count = {}

for i in t:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for i in count:
    print(i,"occurence: ",count[i])
