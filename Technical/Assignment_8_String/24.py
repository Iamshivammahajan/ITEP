def reverse_spelling_words():
    str = input("Enter a string: ")
    s = str.split()
    for word in s:
        print(word[::-1], end = " ")
reverse_spelling_words()
    