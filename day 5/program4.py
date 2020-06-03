print("enter weights of items")
wt = [int(x) for x in input().split()]
print("enter corresponding values of items")
val = [int(x) for x in input().split()]
w = int(input("enter the weight capacity: "))

n = len(wt) #no. of items

T = [[0]*(w+1)]*(n+1) #table which stores value for each(i,wi) where i is the no. of items and wi is the weight capacity left

for i in range(1,n+1):
    for j in range(1,w+1):
        if j>=wt[i-1] and (T[i-1][j-wt[i-1]]+val[i-1])>T[i-1][j]:
            T[i][j] = T[i-1][j-wt[i-1]] + val[i-1]
        else:
            T[i][j] = T[i-1][j]

print("total value in Knapsack is: ",T[n][w])
