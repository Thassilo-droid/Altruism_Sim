"""
V 1.0

Class Aleel
"""
from abc import ABC, abstractmethod

class Aleel(ABC):

    """

    Aleel is the superclass for all living entities in the Environment
    """

    def __init__(self, identity, strength, fertability, \
                cowardness, hp, fed_scale, is_fed=False, is_alive=True\
                has_reproduced=False, has_partner=False):
        #initializing everything
        self.identity = identity
        self.strength = strength
        self.fertability = fertability
        self.cowardness = cowardness
        self.hp = hp
        self.fed_scale = fed_scale
        self.is_fed = is_fed
        self.is_alive = is_alive
        self.has_reproduced = has_reproduced
        self.has_partner = has_partner
        #partner for reproduction
        self.partner = None

    def eat(self, food):
        """
        eats the food and adds to fed scale
        """
        #adds nutrients to fed scale
        self.fed_scale += food.nutrients
        #setting is_fed
        self.is_fed = True

    def reproduce(self, other):
        """
        checking own parameters for reproduction
        """
        #checking if not already has partner
        if not self.has_partner:
            #setting partner
            self.has_partner = True
            self.partner = other

        #starting reproducing process
        self.has_reproduced = True

        return type(self)

    def obtain_foot(self, foodresource):
        """
        obtains food from the resource
        """
        gotten = foodresource.givefood()
        self.eat(gotten)



    def find_home(self, homes):
        #not yet defined
        pass
