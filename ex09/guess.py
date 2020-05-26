import random


print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out ", end="")
print("the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
nbr = random.randint(0, 100)
i = 0
endLoop = False
while endLoop is False:
    guess = input("What's your guess between 1 and 99?\n")
    if guess == "exit" or str.isnumeric(guess) is False:
        endLoop = True
    elif int(guess) < nbr:
        print("Too low!")
    elif int(guess) > nbr:
        print("Too high!")
    else:
        if nbr == 42:
            print("The answer to the ultimate question of life, ", end="")
            print("the universe and everything is 42.")
        if i == 0:
            print("Congratulations, you've got it on your first try")
        else:
            print("Congratulations, you've got it!")
        endLoop = True
    i += 1
if str.isnumeric(guess) and i > 1:
    print("You won in {} attempts!".format(i))
