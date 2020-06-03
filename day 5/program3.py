print("enter values of houses:")
house = [int(x) for x in input().split()]

ans = [0]*len(house)# ith value stores the maximum value attained till ith value of 'house'

ans[0] = house[0]
ans[1] = max(house[0],house[1])

for i in range(2,len(house)):
    #the ith value of 'house' has 2 options- whether to be taken or not
    #if taken then max of i-2 values will be considered
    #if not taken then i-1 values will be cosidered
    ans[i] = max(house[i] + ans[i-2], ans[i-1])

print("the robber can steal maximum:",ans[-1],"amount")
