def twostringequal():
    str1 = input("Enter a string: ")
    str2 = input("Enter a string: ")
    if len(str1) != len(str2):
        print("Strings are not equal")
        return
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print("Strings are not equal")
            return
    print("Strings are equal")
twostringequal()