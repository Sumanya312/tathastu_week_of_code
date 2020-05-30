cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))

profit = sp-cp

new_profit = 5 + (profit*100)/cp
new_sp = cp*(1 + new_profit/100)
 
print("Profit from above sell is: ",profit)
print("Selling Price for increasing profit by 5% is: ",new_sp)
