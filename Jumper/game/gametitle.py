import os
import shutil

class GameTitle():

    def __init__(self) -> None:
        self._terminal_size = shutil.get_terminal_size().columns

    def clearConsole(self) -> None:

        if os.name in ("nt", "dos"):
            os.system("cls")
        else:
            os.system("clear")

    def PrintGameTitle(self, game_title) -> None:

        title = f'{game_title}  - \U0001f601   \n'
        print(title.center(self._terminal_size))
