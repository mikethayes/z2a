#!/bin/python3
from tqdm import tqdm
from time import sleep
import re
import os

letters = 'zyxwvutsrqponmlkjihgfedcba'

def main():
    words = ["Lemonade", "Frangipan", "Exotica", 'Antidisestablishmentarianism', 'Waxahatchee']

    guess_words = []

    for w in words:
        guess_words.append(GuessWord(w))

    for x in letters:
        os.system('cls||echo -e \\\\033c')
        print(make_legend(x))
        for gw in guess_words:
            gw.guess_letter(x)
            print(gw)

        print()
        for i in tqdm(range(10)):
            sleep(0.05)

def make_legend(letter):
    legend = ""

    for l in letters:
        if l == letter:
            legend = legend + color.BOLD + color.RED + l.capitalize() + color.END
        else:
            legend += l

    return legend


class GuessWord():
    def __init__(self, word):
        self.word = word
        self.guess = ['_'] * len(self.word)

    def guess_letter(self, letter):
        for i in range(0, len(self.word)):
            if (self.word[i].lower() == letter):
                self.guess[i] = self.word[i]

    def __str__(self):
        return " ".join(self.guess)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


if __name__ == "__main__":
    main()