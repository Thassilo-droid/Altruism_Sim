"""
V 1.0

Class Enemy
"""


class Enemy():

    """

    superclass of Panther, etc.
    """

    def __init__(self, species, name, age, sex, appetite, rage, size, strength):
        self.species = species
        self.name = name
        self.age = age
        self.sex = sex
        self.appetite = appetite
        self.rage = rage
        self.size = size
        self.strength = strength

    def succesfullhunt(self):
        """
        had a succesfull hunt, as conclusion the apetite gets lower
        """
        self.appetite -= 1
