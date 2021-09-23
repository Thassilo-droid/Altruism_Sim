"""
V 1.0

Class Enemy
"""

import random

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

    def fightwithaleel(self, other):
<<<<<<< HEAD
        self.strength += random.choice(1, 7)    """Enemy rolls Dice int gets addded to Strenght """
        other.strength += random.choice(1, 7)   """Aleel rolls Dice int gets added to Strength """
        if self.strenght > other.strength:      """ """
            enemykillsaleel = true              """ """
        else:                                   """ """
            enemykillsaleel = false             """ """
=======
        """
        -> Später kampf erhöht Stärke
        """
        estrength = self.strength
        ostrength = other.strength
        estrength += random.choice(1, 7)
        ostrength += random.choice(1, 7)
        if estrength > ostrength:
            return True
        else:
            return False
>>>>>>> eb4967bc30dc78094ceeab57d1d265448779860b

    def succesfullhunt(self):
        """
        had a succesfull hunt, as conclusion the apetite gets lower
        """
        self.appetite -= 1
