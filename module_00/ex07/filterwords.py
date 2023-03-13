from sys import argv
from string import punctuation

args = argv[1:]

if len(args) == 2:
    
    try:
        number = int(args[1])
        filtered = args[0]
        for c in punctuation:
            filtered = filtered.replace(c, '')
        lst = filtered.split(" ")
        lst = [item for item in lst if len(item) > number]
        print(lst)
    except:
        print("ERROR")
else:

    print("ERROR")
