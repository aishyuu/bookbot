import re

file_path = "./books/frankenstein.txt"

with open(file_path, "r") as f:
    file_contents = f.read()
    words = file_contents.lower().replace(" ", "")
    res = re.sub(r'[^a-zA-Z]', '', words)
    letter_count = {}
    for letter in res:
        if letter not in letter_count.keys():
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    for key in letter_count.keys():
        print(f"The '{key}' character was found {letter_count[key]} times")