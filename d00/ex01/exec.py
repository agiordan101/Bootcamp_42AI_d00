import sys


def rev_print(str):
    lenstr = len(str)
    for i in range(lenstr):
        c = str[lenstr - 1 - i]
        if (c.isupper()):
            print(c.lower(), end="")
        else:
            print(c.upper(), end="")


lenargs = len(sys.argv)
for i in range(0, lenargs - 1):
    if (i != 0):
        print(" ", end="")
    rev_print(sys.argv[lenargs - 1 - i])
