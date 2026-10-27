def duplicateremove():
    str = input("Enter a string: ")
    result = ""
    for ch in str:
        if ch not in result:
            result += ch
    print(result)
duplicateremove()