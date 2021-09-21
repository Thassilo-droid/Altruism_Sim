"""
V.1.0

Class Food
"""


class Food():

    """

    superclass of Apple, Mango, etc.
    """

    def __init__(self, species, nutrients, age, condition):
        self.species = species
        self. nutrients = nutrients
        self.age = age
        self.condition = condition

    def getspoiled(self):
        if age > 5:
            condtion = {"spoiled": 0}
