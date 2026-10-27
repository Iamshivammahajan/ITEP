def firstnonrepeat():
    str = input("Enter a string: ")
    for ch in str:
        if str.count(ch) == 1:
            print(ch)
            break
    else:
        print("No non-repeating character")
firstnonrepeat()
