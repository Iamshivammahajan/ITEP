classes = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))

percentage = attended / classes * 100

print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")
