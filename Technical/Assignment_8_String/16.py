def anagram():
    str1 = input("Enter a string: ")
    str2 = input("Enter a string: ")
    if sorted(str1) == sorted(str2):
        print(f"{str1} and {str2} are anagrams")
    else:
        print(f"{str1} and {str2} are not anagrams")
anagram()