"""
V 1.0

Class Enemy
"""


class Enemy():

    """

    superclass of Panther, etc.
    """

    def __init__(self, species, name, age, sex, apetite, rage, size, strength):
        self.species = species
        self.age = age
        self.sex = sex
        self.apetite = apetite
        self.rage = rage
        self.size = size
        self.strength = strength

    def succesfullhunt(self):
        """
        had a succesfull hunt, as conclusion the apetite gets lower
        """
        self.apetite -= 1
