def check_only_digit():
    str = input("Enter a string : ")
    flag=True
    for word in str:
        if word not in "0123456789":
            flag=False
            break
    if flag:
        print("Only digits")
    else:
        print("Not only digits")
check_only_digit() 