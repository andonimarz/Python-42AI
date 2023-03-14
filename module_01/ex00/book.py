from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipes_list = {"entrante": [], "comida": [], "postre": []}

    def get_recipe_by_name(self, name):
        """Imprime la receta con el nombre name y devuelve la instancia"""
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(f"No se encontró ninguna receta con el nombre {name}")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type"""
        if recipe_type not in self.recipes_list:
            print(f"No se encontró ningún tipo de receta con el nombre {recipe_type}")
            return []
        recipes = self.recipes_list[recipe_type]
        for recipe in recipes:
            print(recipe)
        return recipes

    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        if not isinstance(recipe, Recipe):
            raise ValueError("Debe añadir una instancia de la clase Recipe")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        print("Updated at: ", self.last_update)

