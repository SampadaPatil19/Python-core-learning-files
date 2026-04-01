# Destructor
"""
1.Special method called automatically
    - when life cycle of object is completed
    - object is destroyeed or deleted
2. use __del__ as name destructor
3. USE: Implement resource delocation, network port closing, database connection detroying
"""


class Cricketer:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
    
    def getData(self):
        print(f"NAME: ",self.name)
        print(f"AGE: ",self.age)
        print(f"ROLE: ",self.role)

    def __del__(self):
        print('Destructor Called.')

c1 = Cricketer('Sachin Tendulkar', 50, 'Batsman')
# del c1
c1.getData()