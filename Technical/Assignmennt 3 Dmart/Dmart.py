print("              D-MART")
print("--------------------------------")

name = input("Enter Customer Name: ")
date = input("Enter Date: ")

# Product 1
item1 = input("Enter Item 1 Name: ")
q1 = int(input("Enter Quantity: "))
p1 = float(input("Enter Price: "))

a1 = q1 * p1

if q1 > 4:
    d1 = a1 * 5 / 100
else:
    d1 = 0

ad1 = a1 - d1


# Product 2
item2 = input("Enter Item 2 Name: ")
q2 = int(input("Enter Quantity: "))
p2 = float(input("Enter Price: "))

a2 = q2 * p2
d2 = 0
ad2 = a2 - d2


# Product 3
item3 = input("Enter Item 3 Name: ")
q3 = int(input("Enter Quantity: "))
p3 = float(input("Enter Price: "))

a3 = q3 * p3
d3 = 0
ad3 = a3 - d3


# Product 4
item4 = input("Enter Item 4 Name: ")
q4 = int(input("Enter Quantity: "))
p4 = float(input("Enter Price: "))

a4 = q4 * p4
d4 = 0
ad4 = a4 - d4


# Product 5 - 10% discount
item5 = input("Enter Item 5 Name: ")
q5 = int(input("Enter Quantity: "))
p5 = float(input("Enter Price: "))

a5 = q5 * p5
d5 = a5 * 10 / 100
ad5 = a5 - d5


# Product 6
item6 = input("Enter Item 6 Name: ")
q6 = int(input("Enter Quantity: "))
p6 = float(input("Enter Price: "))

a6 = q6 * p6
d6 = 0
ad6 = a6 - d6


# Product 7
item7 = input("Enter Item 7 Name: ")
q7 = int(input("Enter Quantity: "))
p7 = float(input("Enter Price: "))

a7 = q7 * p7
d7 = 0
ad7 = a7 - d7


# Product 8
item8 = input("Enter Item 8 Name: ")
q8 = int(input("Enter Quantity: "))
p8 = float(input("Enter Price: "))

a8 = q8 * p8
d8 = 0
ad8 = a8 - d8


# Product 9
item9 = input("Enter Item 9 Name: ")
q9 = int(input("Enter Quantity: "))
p9 = float(input("Enter Price: "))

a9 = q9 * p9
d9 = 0
ad9 = a9 - d9


# Product 10 - 15% discount
item10 = input("Enter Item 10 Name: ")
q10 = int(input("Enter Quantity: "))
p10 = float(input("Enter Price: "))

a10 = q10 * p10
d10 = a10 * 15 / 100
ad10 = a10 - d10


# Total after product discounts
total = ad1 + ad2 + ad3 + ad4 + ad5 + ad6 + ad7 + ad8 + ad9 + ad10


# Bill-level discount
if total > 10000:
    bill_discount = total * 15 / 100
elif total >= 5000:
    bill_discount = total * 10 / 100
else:
    bill_discount = 0

after_bill_discount = total - bill_discount


# Gender and Gift
gender = input("Enter Gender (Male/Female): ")

if gender.lower() == "female":
    gift = "Cadberry"
else:
    gift = "Ledger Wallet"


# Carry Bag
bag = input("Do you want Carry Bag? (yes/no): ")

if bag.lower() == "yes":
    bag_charge = 10
else:
    bag_charge = 0


# GST
gst = after_bill_discount * 10 / 100

final_amount = after_bill_discount + gst + bag_charge


# BILL
print("\n\n========================================")
print("                  D-MART")
print("========================================")
print("Name :", name)
print("Date :", date)

print("----------------------------------------")
print("Item       Quantity       Price")
print("----------------------------------------")

print(item1, "     ", q1, "          ", p1)
print(item2, "     ", q2, "          ", p2)
print(item3, "     ", q3, "          ", p3)
print(item4, "     ", q4, "          ", p4)
print(item5, "     ", q5, "          ", p5)
print(item6, "     ", q6, "          ", p6)
print(item7, "     ", q7, "          ", p7)
print(item8, "     ", q8, "          ", p8)
print(item9, "     ", q9, "          ", p9)
print(item10, "    ", q10, "          ", p10)

print("----------------------------------------")
print("Total After Product Discount :", total)
print("Bill Discount                :", bill_discount)
print("Gift                         :", gift)
print("Carry Bag                    :", bag_charge)
print("GST (10%)                    :", gst)

print("----------------------------------------")
print("FINAL AMOUNT                 :", final_amount)
print("----------------------------------------")

print("             Thank You")
print("              To Visit")
print("               D-MART")