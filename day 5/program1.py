n = int(input("enter an integer: "))

new_num = 0
temp = n
c = 0
while(temp!=0):
    d = temp%10
    if d==0:
        d=5
    new_num = new_num + d*(10**c)
    c+=1
    temp = temp//10

print("new number is: ",new_num)
