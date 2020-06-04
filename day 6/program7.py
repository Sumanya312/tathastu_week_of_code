def ackermann(m,n):
    if m==0:
        return(n+1)
    if n==0 and m>0:
        return ackermann(m-1,1)
    if m>0 and n>0:
        return ackermann(m-1,ackermann(m,n-1))


print("enter two values: ",end="")
a,b = [int(x) for x in input().split()]
res = ackermann(a,b)
print("ackermann of (",a,",",b,") is:",res )
