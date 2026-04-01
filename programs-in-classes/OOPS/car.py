# Constructor in Python
"""
1. Special Method
2. Called automatically when an Object of the class is created.
3. Use to implement the compulsory task.
4. Line of code is write in constructor those will be executing compulsorily.
5. use __init__ name for constructor
6. Types: Default & Parameterized Constructor
"""

class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def getData(self):
        data = 'BRAND: ' + self.brand
        data += '\nCOLOR: '+ self.color
        data +='\nPRICE: '+ str(self.price)
        data += '\n-------------------'
        return data

c1 = Car('BMW', 'Black', 10000000)
c2 = Car('Tesla', 'White', 500000000)

print(c1.getData())
print(c2.getData())