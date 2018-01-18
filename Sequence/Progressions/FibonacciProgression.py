from Sequence.Progressions.Progression import Progression

class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        '''
        Create a fibonacci progression
        :param self:
        :param first: first fibonacci value
        :param second: second fibonacci value
        :return:
        '''

        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        '''Update the current value by taking a sum of the previous two'''
        self._prev, self._current = self._current, self._current + self._prev

