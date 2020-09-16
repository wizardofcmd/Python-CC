from collections import OrderedDict
from random import randint
dict = OrderedDict()

glossary = {'loop':'iterate', 'variable':'stored data', 'boolean':'if something \
is true or false', 'tuple':'unchangeable piece of data'}

for key, value in glossary.items():
    dict[key] = value
print(dict)

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        die = randint(1, self.sides)
        print(die)

dice = Die(10)
dice.roll_die()
