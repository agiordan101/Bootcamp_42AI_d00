t = (19, 42, 21)
lent = len(t)
print("The" + str(lent) + "numbers are:", end="")
for i in range(lent):
    if i != 0:
        print(",", end="")
    print(" " + str(t[i]), end="")
print()
