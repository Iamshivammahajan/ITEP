quantity = int(input("Enter quantity: "))

cost = quantity * 100

if cost > 1000:
    discount = cost * 10 / 100
    cost = cost - discount

print("Total cost:", cost)