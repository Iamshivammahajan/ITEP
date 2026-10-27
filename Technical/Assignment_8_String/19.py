def freq():
    str = input("Enter a string: ")
    result = {}
    for ch in str:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    print(result)
freq()