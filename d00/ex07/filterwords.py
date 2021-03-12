import sys
import string


if len(sys.argv) < 3 or str.isnumeric(sys.argv[1]) or\
   str.isnumeric(sys.argv[2]) is False or len(sys.argv) > 3:
    print("ERROR")
else:
    text = sys.argv[1]
    lmax = int(sys.argv[2])
    newtext = ""
    for c in text:
        if (c in string.punctuation) is False:
            newtext += c
    words = newtext.split(' ')
    new_words = []
    for w in words:
        if len(w) > lmax:
            new_words.append(w)
    print(new_words)
