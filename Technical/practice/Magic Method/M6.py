class compare:
    def __init__(self,val):
        self.val = val

    def __eq__(self,other):
        return self.val == other.val

a = compare("ABCD")
b = compare("ABCD")
print(a == b)