import sys


morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": ".-",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": " /"
}


def delete_space(text):
    newtext = ""
    for c in text:
        if c != " ":
            newtext += c
    return newtext


del sys.argv[0]
for i in range(len(sys.argv)):
    if (i != 0):
        print("/ ", end="")
    if delete_space(sys.argv[i]).isalnum() is False:
        print("ERROR", end="")
    else:
        for c in sys.argv[i]:
            print(morse[c.lower()], end=" ")
if len(sys.argv):
    print()
