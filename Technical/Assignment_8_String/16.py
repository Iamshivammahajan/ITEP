def anagram():
    str1 = input("Enter a string: ")
    str2 = input("Enter a string: ")
    for ch in str1:
        if ch not in str2:
            print("Not an anagram")
            return
    for ch in str2:
        if ch not in str1:
            print("Not an anagram")
            return
    print("Anagram")
anagram()