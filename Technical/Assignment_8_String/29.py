#Remove a particular character from a string without using replace().
def remove_char(str,char):
    result = ""
    for ch in str:
        if ch != char:
            result += ch
    return result
str = input("Enter a string: ")
char = input("Enter the character to remove: ")
print(remove_char(str,char))