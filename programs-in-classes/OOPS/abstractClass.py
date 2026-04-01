# ABSTRACT CLASSES
"""
1. Generic classes.
2. At least one abstract method should be present.
3. Can't instantiate(creating Object) of abstract class.
"""

# ABSTRACT METHOD
"""
1. method having only definition without body.
2. It should be implement in subclasses.
"""

# HAS-A RELATIONSHIP
"""

"""

from abc import ABC, abstractmethod

class Warrior(ABC):

    @abstractmethod
    def fight():
        pass

class ArcheryWorrior(Warrior):
    def fight(self):
        print('Archery Worrior uses Archer to fight.')

class MaceWorrior(Warrior):
    def fight(self):
        print('Mace Worrior uses Mace(gada) to fight.')

class SwordWorrior(Warrior):
    def fight(self):
      print('Aword Worrior uses Swords to fight.')


arch = ArcheryWorrior()
mace = MaceWorrior()
sword = SwordWorrior()

list_of_object = [arch, mace, sword]
for obj in list_of_object:
    obj.fight()
