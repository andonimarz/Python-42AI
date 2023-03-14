import random

def list_randomizer(lst):
    result = []
    while len(lst) > 0:
        index = random.randrange(0,len(lst))
        result.append(lst.pop(index))
    return result

def generator(text, sep=" ", option=None):
    '''
    Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
    option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
    '''

    if isinstance(text, (str)) == False or text.isprintable() == False :
        print("ERROR")
    else:
        lst = text.split(sep)

        if option == "shuffle":
            lst = list_randomizer(lst)
        if option == "unique":
            lst = [*set(lst)]
        if option == "ordered":
            lst = sorted(lst)
        for word in lst:
            yield word


if __name__ == "__main__":
    print("== SHUFFLE ==")
    for word in generator("prueba1 prueba2 prueba2 prueba3 prueba4 prueba5", " ", "shuffle"):
        print(word)
    print()
    print("== UNIQUE ==")
    for word in generator("prueba1 prueba1 prueba2 prueba2 prueba2 prueba3", " ", "unique"):
        print(word)
    print()
    print("== ORDERED ==")
    for word in generator("pruebaF pruebaA pruebaA pruebaD pruebaB pruebaC pruebaE", " ", "ordered"):
        print(word)
    print()
    print("== ERROR ==")
    for word in generator(1234, " ", "ordered"):
        print(word)
    print()