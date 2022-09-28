import random

class Hider:

    def __init__(self):
        ''' This method contructs a new hider
        '''
        self._location = random.randint(1, 1000)
        self._distance = [0, 0]

    def get_hint(self):
        ''' This method will give hints to help the user to find the hider
        '''
        hint = "(-.-) Nap time."
        if self._distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "(>.<) Getting warmer!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) Getting colder!"
        return hint

    def is_found(self):
        '''This method defines if the hider was found or not'''
        return (self._distance[-1] == 0)

    def watch_seeker(self, seeker):
        '''This method calculates the distance between the seeker and the hider
        '''
        distance = self._location - seeker.get_location()
        self._distance.append(distance)