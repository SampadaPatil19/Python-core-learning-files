class Person:
    def __init__(self, name, address, balance):
        self.name = name
        self._address = address
        self.__balance = balance
    
    def getData(self):
        print('BALANCE: ',self.__balance)

p1 = Person('Gunjan', 'Amravati', 1200000)
p1.getData()
# print(p1.__balance)

print(p1._Person__balance)  #using different naming convention we are accessing the private attribute