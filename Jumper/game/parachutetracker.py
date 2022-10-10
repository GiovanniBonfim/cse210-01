class ParachuteTracker:

    def __init__(self) -> None:
        self._parachute_index = 0

    def PrintParachute(self) -> list:


        self.parachute = [
            """
            ________
              
             
             
             
               X
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             
             
             
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             
             
              \ /
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             
             \   /
              \ /
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              
             /___\\
             \   /
              \ /
               0
              /|\\
              / \\

            ^^^^^^^
            """,
            """
            ________
              ___
             /___\\
             \   /
              \ /
               0
              /|\\
              / \\

            ^^^^^^^
            """
        ]
        return self.parachute[self._parachute_index]

    def parachuteChoose(self, index=0) -> None:

        self._parachute_index = index
        print(self.PrintParachute())
        