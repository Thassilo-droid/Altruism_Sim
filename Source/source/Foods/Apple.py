from source.Foods.Food import Food

class Apple(Food):

    def __init__(self):
        super().__init__("Apple", 10, 0, {"": None})

    def getspoiled(self):
        if age >= 30:
            condition = {"spoiled": 0}
            nutrients -= 0.5*nutrients
