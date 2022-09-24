import random

class Card:
    """ This class will define the cards of the game
    """

    def __init__(self) -> None:
        self.value = 0

    def roll_card(self):
        self.value = random.randint(1, 13)
        return self.value