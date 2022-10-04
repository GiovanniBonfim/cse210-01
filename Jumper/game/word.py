import random

class Word:

    def __init__(self):

        self.words = ["water","leaf","screen","elephant","computer","happy"]
        self.chosen_word = ""

    def random_word(self):

        self.chosen_word = random(self.words)
