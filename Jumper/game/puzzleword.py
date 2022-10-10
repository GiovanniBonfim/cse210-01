import random


class PuzzleWord:

    def __init__(self) -> None:
        
        self._wordlist = []

    def randomWord(self):
        self.load_list()
        my_random_word = random.choice(self._wordlist)
        return my_random_word.upper()

    def load_list(self) -> None:

        with open("words.txt", "rt") as text_file:
            read_data = text_file.readlines()
            for line in read_data:
                clean_line = line.strip()
                self._wordlist.append(clean_line)