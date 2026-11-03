class mul:
    def __init__(self,value):
        self.value = value

    def __mul__(self,others):
        return self.value * others.value

n1 = mul(10)
n2 = mul(5)
result = n1 * n2
print(result)
