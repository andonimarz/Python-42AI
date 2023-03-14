class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

        # Validar la entrada de los atributos
        if not isinstance(self.name, str) or len(self.name) == 0:
            raise ValueError("El nombre de la receta debe ser un string no vacío")

        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl not in range(1, 6):
            raise ValueError("El nivel de cocina debe ser un número entero entre 1 y 5")

        if not isinstance(self.cooking_time, int) or self.cooking_time < 0:
            raise ValueError("El tiempo de cocción debe ser un número entero no negativo")

        if not isinstance(self.ingredients, list) or len(self.ingredients) == 0:
            raise ValueError("La lista de ingredientes debe ser una lista no vacía")

        if not isinstance(self.recipe_type, str) or self.recipe_type not in ["entrante", "comida", "postre"]:
            raise ValueError("El tipo de receta debe ser una de las siguientes opciones: entrante, comida, postre")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Nombre: {self.name}\nNivel de cocina: {self.cooking_lvl}\nTiempo de cocción: {self.cooking_time} minutos\nIngredientes: {', '.join(self.ingredients)}\nTipo de receta: {self.recipe_type}\n"
        if self.description:
            txt += f"Descripción: {self.description}\n"
        return txt
