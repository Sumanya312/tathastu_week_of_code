s = input("enter a string: ")

count = {}

for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

one=0
c=0

for i in count:
    if count[i]%2==1:
        if one ==0:
            one=1
        elif one ==1:
            c+=1

print("minimum characters to be removed: ",c)
