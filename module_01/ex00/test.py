from book import Book
from recipe import Recipe

print("===========__CREATE__===========")
try:
    tortilla = Recipe("Tortilla de patatas", 3, 30, ["patatas", "huevos", "cebolla", "aceite", "sal"], "Una clásica tortilla española", "comida")
    ensalada = Recipe("Ensalada de tomate", 1, 10, ["tomates", "cebolla", "aceite", "vinagre", "sal"], "Una sencilla ensalada de tomate", "entrante")
    bad_recipe = Recipe("Bad_recipe", 6, 10, ["tomates", "cebolla", "aceite", "vinagre", "sal"], "Una sencilla ensalada de tomate", "entrante")
except ValueError as e:
    print(e)

print("===========___STR___===========")
to_print = str(tortilla)
print(to_print)
to_print = str(ensalada)
print(to_print)

print("===========___ADD___===========")
try:
    libro = Book("librillo")
    libro.add_recipe(tortilla)
    libro.add_recipe(ensalada)
    libro.add_recipe(libro)
except ValueError as e:
    print(e)

print("===========___GET_BY_NAME___===========")
to_print = libro.get_recipe_by_name("Tortilla de patatas")
print(to_print)
print("_______________________________________")
to_print = libro.get_recipe_by_name("sjnnsfd")
print(to_print)

print("===========___GET_BY_TYPE___===========")
to_print = libro.get_recipes_by_types("entrante")
print(to_print)
print("_______________________________________")
to_print = libro.get_recipes_by_types("comida")
print(to_print)