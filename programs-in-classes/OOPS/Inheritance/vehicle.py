# Inheritence - create a class of Vehicle and a subclass Car of it.

class Vehicle:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def getData(self):
        print(f"BRAND: {self.brand}\nCOLOR: {self.color}\nPRICE:{self.price}")

class Car(Vehicle):
    def __init__(self, brand, color, price, sunroof):
        super().__init__(brand, color, price)
        self.sunroof = sunroof

    def getData(self):
        super().getData()
        print(f'SUNROOF: {self.sunroof}')

c1 = Car('Tesla', 'black', 20000000, 'Available')
c1.getData()
print(c1.brand)