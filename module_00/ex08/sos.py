import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

args = ""
argnum = len(sys.argv)

if argnum == 2:
    args = sys.argv[1]

elif argnum > 2:
    for item in sys.argv[1:]:
        args = args + ' ' + item
else:
    quit()


output = ""
try:
    for char in args:
        char = char.upper()
        if char in MORSE_CODE_DICT:
            output = output + MORSE_CODE_DICT[char]
        elif char == " ":
            output = output + "/"
        else:
            raise Exception()
except:
    print("ERROR")
print(output)
