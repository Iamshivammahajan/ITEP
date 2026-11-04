physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
biology = int(input("Enter Biology marks: "))
maths = int(input("Enter Mathematics marks: "))
computer = int(input("Enter Computer marks: "))

total = physics + chemistry + biology + maths + computer
percentage = total / 5

print("Percentage:", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")    