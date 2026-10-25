price = float(input("Enter cost price of bike: "))

if price > 100000:
    tax = price * 15 / 100
elif price > 50000:
    tax = price * 10 / 100
else:
    tax = price * 5 / 100

print("Road tax:", tax)