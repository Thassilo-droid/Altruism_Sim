from source.Foods.Food import Food

class Banana(Food):

    def __init__(self):
        super().__init__("Banana", 30, 0, {"": None})

    def getspoiled(self):
        if age >= 10:
            condition = {"spoiled": 0}
            nutrients -= 0.5*nutrients
