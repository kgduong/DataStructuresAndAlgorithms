class Progression:
    '''Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2, ...
    '''
    def __init__(self, start=0):
        '''Initialize current progression to first value'''
        self._current = start

    def _advance(self):
        '''
        Update self._current to new value

        Should be overridden by subclass
        '''
        self._current +=1

    def __next__(self):
        '''Returns next item or else raise StopIteration error'''
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        '''by convention, an iterator must return itself as the iterator'''
        return self

    def print_progression(self, n):
        '''Print n next values of the progression'''
        print(' '.join(str(next(self)) for j in range(n))) #uses __next__ for n values

