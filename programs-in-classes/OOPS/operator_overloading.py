class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
    
    def __add__(self, other):
        s = self.s + other.s
        m = s // 60
        self.s = s % 60

        m = m + self.m + other.m
        h = m // 60
        self.m = m % 60

        self.h = h + self.h + other.h

        # return f'{h} : {m} : {s}'
        return self
    
    def __str__(self):
        return f'{self.h} : {self.m} : {self.s}'
    
t1 = Time(10, 45, 30)
t2 = Time(5, 25, 40)
# t3 = Time(5, 25, 40)

print(t1 + t2)