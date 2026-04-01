class Animal:
    def sound(self):
        print('Sound of Animals.')

class Dog(Animal):
    def sound(self):
        return 'Bark.'

dog1 = Dog()
print(dog1.sound())