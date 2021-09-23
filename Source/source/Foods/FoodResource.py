"""
V 1.0

Class FoodResource
"""
import random

class FoodResource():

    """


    """

    def __init__(self, FoodQuantity, Foods, EnemyExistence, \
                Enemy, free_places, places):

        self.FoodQuantity = FoodQuantity
        self.Foods = Foods
        self.EnemyExistence = EnemyExistence
        self.Enemy = Enemy
        self.free_places = free_places
        self.places = places

    def givefood(self):
        """
        gives back food
        """
        keys = list(self.Foods.keys())
        choice = random.choice(keys)

        max_rot = len(keys)

        while self.Foods[choice] <= 0 and max_rot > 0:
            keys.remove(choice)
            choice = random.choice(keys)
            if self.Foods[choice] > 0:
                max_rot -= 1
        #minus
        self.Foods[choice] -= 1
        #
        return choice()
