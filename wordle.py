import random
import json

class Attempt:
    def __init__(self, error, output):
        self.error = error
        self.output = output
        
class Wordle:
    def __init__(self, all_words:bool=False, hard:bool=False):
        self.word = self.random_word()
        self.guesses = []
        self.all_words = all_words
        self.hard = hard
    
    def load_words(self):
        f = open("./vocab.json")
        j = json.load(f)
        f.close()
        if self.all_words:
            return j["wordle"]["vocab"] + j["wordle"]["other"]
        return j["wordle"]["vocab"]
    
    def random_word(self):
        words = self.load_words()
        self.word = random.choice(words)
    
    def valid(self, w:str):
        if len(w) != len(self.word):
            return False
        if self.hard and len(self.guesses) > 0:
            for i in range(len(w)):
                if self.guesses[-1][i] == self.word[i] and self.word[-1][i] != w[i]:
                    return False
        return True
    
    def guess(self, w:str) -> list[int]:
        """ if not vaild returns []"""
        if self.vaild(w):
            x = self.robo_guess(w)
    
    def robo_guess(self, w:str):
        """This Function assumes input is always vaild
            list[i] == 0 => w[i] not in word
            list[i] == 1 => w[i] in word
            list[i] == 2 => w[i] is in correct place
        """
        
        out = [] * len(self.word)
        self.guesses.append(w)
        # checks if weather that letter is in the word.
        for i in w:
            if i in self.word:
                out.append(1)
            else:
                out.append(0)
    
        # checks if the word is at the position 
        for i in len(out):
            if w[i] == self.word[i]:
                out[i] = 2
        return out