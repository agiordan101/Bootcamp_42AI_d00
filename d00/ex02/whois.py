import sys

if (len(sys.argv) == 1):
    exit()
if (len(sys.argv) > 2 or
   (len(sys.argv) == 2 and str.isnumeric(sys.argv[1]) is False)):
    print("ERROR")
elif (int(sys.argv[1]) == 0):
    print("I'm Zero.")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
