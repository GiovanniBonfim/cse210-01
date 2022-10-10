from game.puzzleword import PuzzleWord


class WordSlicer:

    def __init__(self) -> None:
        
        self._word = PuzzleWord().randomWord()

    def slicer(self) -> list:

        self.sliced_word = list(self._word)
        return self.sliced_word