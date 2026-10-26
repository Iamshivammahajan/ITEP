def removedigit():
    str1 = input("Enter a string: ")
    result = ""
    for ch in str1:
        if ch not in "0123456789":
            result += ch
    print(result)
removedigit()   
