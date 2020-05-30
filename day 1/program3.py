a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Values before swapping are :",a," ",b)

a = a+b
b = a-b
a = a-b

print("Values after swapping are :",a," ",b)
