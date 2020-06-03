print("enter a list of integers:")
l = [int(x) for x in input().split()]

size = len(l)

odd = []
even = []

for i in range(size):
    if l[i]%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])

even.sort()
odd.sort(reverse=True)

res = even + odd
print("updated list is: ",res)
