import json
from difflib import get_close_matches
data = json.load(open("data.json"))

word = input("Enter word please:")


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        YN = input('Did you mean %s? Please enter Y if Yes, or N for No:' %
                   get_close_matches(w, data.keys())[0])
        if YN == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif YN == "N":
            return "word does not exist, please double check!"
        else:
            return "I do not understand your entry."
    else:
        return "word does not exist, plese double check!"


output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
