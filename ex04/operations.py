import sys

if len(sys.argv) != 3 or\
   str.isnumeric(sys.argv[1]) is False or\
   str.isnumeric(sys.argv[2]) is False:
    if (len(sys.argv) < 3):
        print(end="")
    elif (len(sys.argv) > 3):
        print("InputError: too many arguments\n")
    else:
        print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum:         " + str(a + b))
    print("Difference:  " + str(a - b))
    print("Product:     " + str(a * b))
    if b == 0:
        print("Quotient:    ERROR (div by zero)")
        print("Reminder:    ERROR (modulo by zero)")
    else:
        print("Quotient:    " + str(a / b))
        print("Reminder:    " + str(a % b))
