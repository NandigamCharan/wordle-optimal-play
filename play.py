import imp
import typer
import json
from wordle import *

def dictionary():
    filepath = "./vocab.json"
    f = open(filepath)
    j = json.load(f)
    f.close()
    return set(j["wordle"]["vocab"]).union(set(j["wordle"]["other"]))

def letter_freq(words):
    table = {}           # freq table
    for word in words:
        for i in word:
            if i not in table:
                table[i]  = 0
            table[i] += 1
    return table


hard = False
all_words = False
wordle = Wordle(False, True)

def play_easy(wordle):
    def best(words):
        pass
    
    picks = {}
    words = dictionary()
    freq = sorted(list(letter_freq(words).items()), key= lambda x: x[1])
    print(freq)


print(play_easy(wordle))