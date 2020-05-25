import sys

if len(sys.argv) != 3 or
    sys.argv[1].isnumeric is not True or
    sys.argv[2].isnumeric is not True:
    if (len(sys.argv) < 3):
    elif (len(sys.argv) > 3):
        print("InputError: too many arguments\n")
    else:
        print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
a = int(sys.argv[1])
b = int(sys.argv[2])
print("Sum:" + str(a + b))
print("Difference:\t" + str(a - b))
print("Product:\t\t" + str(a * b))
print("Quotient:\t\t" + str(a / b))
print("Reminder:\t\t" + str(a % b))