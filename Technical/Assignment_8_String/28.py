#Check whether one string is a rotation of another.
def rotation(str1,str2):
    if len(str1)!=len(str2):
        return False
    temp=str1+str1
    if str2 in temp:
        return True
    else:
        return False
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
if rotation(str1,str2):
    print("The second string is a rotation of the first string")
else:
    print("The second string is not a rotation of the first string")