class Recipe:
    def __init__(self,id,image,missedIngredients,unusedIngredients):
        self.id = id
        self.image = image
        self.missedIngredients = missedIngredients
        self.unusedIngredients = unusedIngredients