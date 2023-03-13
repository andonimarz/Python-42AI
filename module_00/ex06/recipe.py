
bocadillo={"ingredients" : ["jamon","pan","queso","tomate"], "meal" : "almuerzo", "prep_time" : 10}
tarta={"ingredients" : ["harina","azucar","huevos"], "meal" : "postre", "prep_time" : 60}
ensalada={"ingredients" : ["aguacate","rucula","tomates","espinacas"], "meal" : "almuerzo", "prep_time" : 15}

cookbook={"bocadillo" : bocadillo, "tarta" : tarta, "ensalada" : ensalada}

def printRecipes():
    print("Recipes in cookbook = ",cookbook.keys())

def printValues():
    print("Please enter a recipe name to get its details:")
    str = input(">> ")
    if str in cookbook:
        print("Ingredients list:", cookbook[str]["ingredients"])
        print("To be eaten for", cookbook[str]["meal"])
        print("Takes", cookbook[str]["prep_time"], "minutes of cooking")
    else:
        print(str, "Sorry, this option does not exist.")

def popRecipe():
    print("Please enter a recipe name to remove:")
    str = input(">> ")
    if str in cookbook:
        cookbook.pop(str)
    else:
        print(str, "Sorry, this option does not exist.")

def addRecipe():
    print("Enter a name:")
    name = input(">> ")
    print("Enter ingredients:")
    lst = []
    while True:
        ingred = input(">> ")
        if len(ingred):
            lst.append(ingred)
        else:
            break
    print("Enter a meal type:")
    meal = input(">> ")
    print("Enter a preparation time:")
    time = input(">> ")
    recipe = {"ingredients" : lst, "meal" : meal, "prep_time" : int(time)}
    cookbook[name] = recipe

print("Welcome to the Python Cookbook !")
while True:
    print("List of available option:")
    print(" 1: Add a recipe")
    print(" 2: Delete a recipe")
    print(" 3: Print a recipe")
    print(" 4: Print the cookbook")
    print(" 5: Quit")
    print("")
    print("Please select an option")

    try:
        option = int(input(">> "))
        print("")
        if option == 1:
            addRecipe()
        elif option == 2:
            popRecipe()
        elif option == 3:
            printValues()
        elif option == 4:
            printRecipes()
        elif option == 5:
            break
        else:
            print("Sorry, this option does not exist")
    except ValueError:
        print("Invalid chooice")
    print("")
print("Cookbook closed. Goodbye !")
