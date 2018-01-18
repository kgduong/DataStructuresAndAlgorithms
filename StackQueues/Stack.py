class ArrayStack:
    '''A stack implemented using an adapted Python list'''

    def __init__(self):
        '''Create an initially empty stack'''
        self._data = []

    def __len__(self):
        '''Return the len of the stack'''
        return len(self._data)

    def is_empty(self):
        '''Returns whether the stack is empty'''
        return len(self._data) == 0

    def push(self, e):
        '''Push element e to the top of the stack'''
        self._data.append(e)

    def top(self):
        '''
        Return the element(but not remove) currently at the top of the stack
        Raises ValueError if the stack is empty
        '''
        if self.is_empty():
            raise ValueError("The stack is empty.")
        currentTop = self._data[-1]
        return currentTop

    def pop(self):
        '''Return and remove the element at the top of the stack
           Raise ValueError if the stack is empty'''
        if self.is_empty():
            raise ValueError("The stack is currently empty")
        return self._data.pop()

    
