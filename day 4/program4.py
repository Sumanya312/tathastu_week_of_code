d = {}
size = int(input("enter size of dictionary: "))
for i in range(size):
    k = int(input("enter key: "))
    d[k] = int(input("enter the key value: "))

t = []
d1 = {}
for i in d:
    if d[i] not in t:
        t.append(d[i])
        d1[i]=d[i]


print(d1)
