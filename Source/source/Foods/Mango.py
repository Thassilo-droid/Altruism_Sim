from source.Foods.Food import Food

class Mango(Food):

    def __init__(self):
        super().__init__("Mango", 20, 0, {"": None})

    def getspoiled(self):
        if age >= 20:
            condition = {"spoiled": 0}
            nutrients -= 0.5*nutrients
