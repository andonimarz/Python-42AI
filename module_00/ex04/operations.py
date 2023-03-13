import sys

args = sys.argv[1:]
if (len(args) > 2):
    print("AssertionError: too many arguments")
elif len(args) == 0:
    print("Usage: python operations.py <number1> <number2>")
else:
    try:
        A = int(args[0])
        B = int(args[1])
        print("Sum:         ", A+B)
        print("Difference:  ", A-B)
        print("Product:     ", A*B)
        try:
            print("Quotient:    ",A/B)
        except:
            print("Quotient:    ERROR (division by zero)")
        try:
            print("Remainder:   ",A%B)
        except:
            print("Remainder:   ERROR (module by zero)")
    except:
        print("AssertionError: only integers")

