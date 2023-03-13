import string
import sys

def text_analyzer(my_str=""):
    '''This function counts the number of upper characters, lower characters, 
    punctuation and spaces in a given text.'''

    try:
        if my_str == 'None':
            info  = input("What is the text to analyze? ")
        else:
            info = my_str

        upper = 0
        lower = 0
        punctuation = 0
        space = 0
        total = 0

        for char in info:
            if char.isupper():
                upper += 1
            if char.islower():
                lower += 1
            if char == " ":
                space += 1
            if char in string.punctuation:
                punctuation += 1
            total += 1
        print("The text contains ", total, " character(s):")
        print("- ", upper, " upper letter(s)")
        print("- ", lower, " lower letter(s)")
        print("- ", punctuation, " punctuation mark(s)")
        print("- ", space, " space(s)")
    except TypeError:
        print("AssertionError: argument is not a string")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Error: invalid arg number.") 
    else:
        text_analyzer(args[0])
