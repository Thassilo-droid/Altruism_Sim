from source.Enemy.Enemy import Enemy

class Panther(Enemy):

    def __init__(self, alter):
        super().__init__("Panther", "Klaus", alter, True, 5, 5, 1, 5)
