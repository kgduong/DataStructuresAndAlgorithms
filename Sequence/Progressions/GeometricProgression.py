from Sequence.Progressions.Progression import Progression

class GeometricProgression(Progression):
    '''
    Create a fibonacci progression
    :param Progression:
    :return:
    '''
    def __init__(self, increment=2, start=1):
        '''
        Create a fibonacci progression
        :param self:
        :param first: first fibonacci value
        :param second: second fibonacci value
        :return:
        '''
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        '''Update the current value by taking a sum of the previous two'''
        self._current = self._current * self._increment

