str = input("enter a string: ")
t=""
for i in str:
    if i in t:
        continue
    else:
        t=t+i
print("updated string is: ",t)
