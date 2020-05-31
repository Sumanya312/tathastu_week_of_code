n=int(input("enter a number: "))

if(n%2==0):
    print("number is even")
else:
    print("number is odd")

c=0
for i in range(1,n):
    if (n%i==0):
        c+=1

if(c==1):
    print("number is prime")
else:
    print("number is not prime")

t = n
sum = 0
while(t):
    d=t%10
    sum = sum  + (d**3)
    t=t//10

if(sum==n):
    print("number is armstrong")
else:
    print("number is not armstrong")

t = str(n)
rev = int(t[::-1])
if(rev==n):
    print("number is pallindrome")
else:
    print("number is not pallindrome")
