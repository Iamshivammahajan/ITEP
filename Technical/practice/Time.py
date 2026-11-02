class Time:
    def __init__(self, hrs, minute, sec):
        self.__hrs = hrs
        self.__minute = minute
        self.__sec = sec

    def add(self, new_time):
        t3 = Time(0,0,0)
        t3.__hrs = self.__hrs + new_time.__hrs
        t3.__minute = self.__minute + new_time.__minute
        t3.__sec = self.__sec + new_time.__sec

        if t3.__sec >= 60:
            t3.__minute += 1
            if t3.__minute >= 60:
                t3.__hrs += 1
                t3.__minute -= 60
            t3.__sec -= 60
        return t3

    def display(self):
        print(f"Hours: {self.__hrs} Minute: {self.__minute} Second: {self.__sec}")
  
t1 = Time(1,30,45)
t2 = Time(9,30,20)
t1.display()
t2.display()
# t3.add(t1,t2)
t3 = t1.add(t2)
print("After addition:")
t3.display()