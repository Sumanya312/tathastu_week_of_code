n = int(input("enter a number: "))

f = 0
s = 1
print(f,s, end=" ")
while(s<n):
    t = f+s
    print(t,end=" ")
    f = s
    s = t
