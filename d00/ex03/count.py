import string


def text_analyzer(*args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if len(args) > 1:
        print("ERROR")
    else:
        if len(args) == 0:
            text = input("What is the text to analyse?")
        else:
            text = args[0]
        stats = [0] * 4
        for c in text:
            if c.isupper() is True:
                stats[0] += 1
            elif c.islower() is True:
                stats[1] += 1
            if c in string.punctuation:
                stats[2] += 1
            elif c is " ":
                stats[3] += 1
        print("The text contains " + str(len(text)) + " characters:\n")
        print("- " + str(stats[0]) + " upper letters\n")
        print("- " + str(stats[1]) + " lower letters\n")
        print("- " + str(stats[2]) + " punctuation marks\n")
        print("- " + str(stats[3]) + " spaces")
