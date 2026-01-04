"""2. Create a class Distance with data members as km,m and cm and add following 
methods : 
a.  Constructor 
b.  Destructor 
c.  Overload +,-  operator"""

# 1km = 1000 m
# 1m = 100 cm
# 1km = 100000 cm
# To add and subtract distances, we will convert everything to centimeters for easy calculation.

class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm
    
    def __del__(self):
        print("Distance object is being deleted.")
    
    def to_cm(self):
        total_cm = (self.km * 100000) + (self.m * 100) + self.cm
        return total_cm

    def __add__(self, other):
        total_cm = self.to_cm() + other.to_cm()
        km = total_cm // 100000
        total_cm = total_cm % 100000
        m = total_cm // 100
        cm = total_cm % 100
        return Distance(km, m, cm)
    
    
    def __sub__(self, other):
        total_cm = self.to_cm() - other.to_cm()
        km = total_cm // 100000
        total_cm = total_cm % 100000
        m = total_cm // 100
        cm = total_cm % 100
        return Distance(km, m, cm)
    
    
    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"
    

d1 = Distance(2, 150, 75)
d2 = Distance(1, 850, 50)
d3 = d1 + d2
print("Addition of distances:", d3) 
d4 = d1 - d2
print("Subtraction of distances:", d4)





    
        