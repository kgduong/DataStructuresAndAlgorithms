from Sequence.Progressions.Progression import Progression


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        '''
        Create a new arithmetic progression
        :param increment: fixed increment to add to each term
        :param start: starting initial value
        '''
        super().__init__(start) #using base class constructor
        self._increment = increment

    def _advance(self):
        '''overload _advance to an arithmetic based advancement'''
        self._current += self._increment