"""
V.1.0

Class Food
"""


class Food:

    """

    superclass of Apple, Mango, etc.
    """

    def __init__(self, species, nutrients, age, condition, spoiled_after):
        self.species = species
        self.nutrients = nutrients
        self.age = age
        self.condition = condition
        self.matured_after = matured_after
        self.spoiled_after = spoiled_after

    def getmature(self):
        if self.age >= self.matured_after:
            self.condtion = "matured"
            self.nutrients += 2*self.nutrients

    def getspoiled(self):
        if self.age >= self.spoiled_after:
            self.condition = "spoiled"
            self.nutrients -= 0.9*self.nutrients
