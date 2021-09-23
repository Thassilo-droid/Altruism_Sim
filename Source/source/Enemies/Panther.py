from source.Enemy.Enemy import Enemy

class Panther(Enemy):

    def __init__(self):
        super().__init__("Panther", "Klaus", 69, True, 5, 5, 1, 5)
