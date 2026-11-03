class division:
    def __init__(self, value):
        self.value = value

    def __truediv__(self,other):
        return self.value / other.value

n1 = division(20)
n2 = division(5)
result = n1 / n2
print(result)