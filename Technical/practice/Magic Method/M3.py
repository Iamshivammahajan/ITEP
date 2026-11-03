class minus:
    def __init__(self,value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

val1 = minus(45)
val2 = minus(10)
result = val1 - val2
print(result)
