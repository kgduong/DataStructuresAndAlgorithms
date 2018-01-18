class LinkedQueue:
    '''FIFO queue implementation using a singly linked list for storage.'''

    class _Node:
        '''lightweight, nonpublic class for storing a singly linked node'''
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create an empty queue'''
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self):
        '''Returns the overall size of the queue'''
        return self._size

    def is_empty(self):
        '''Returns whether the queue is empty or not'''
        return self._size == 0

    def first(self):
        '''Returns but do not remove the element at the front of the queue'''
        if (self.is_empty()):
            raise ValueError("The queue is currently empty.")
        return self._head._element

    def dequeue(self):
        '''Remove and return the first element of the queue(LIFO)'''
        if(self.is_empty()):
            raise ValueError("The queue is currently empty.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if(self.is_empty()):
            self._tail = None #special case if the last element is removed, set tail to None as well
        return answer

    def enqueue(self, e):
        '''Add an element to the back of the queue'''
        newest = self._Node(e, None)
        if(self.is_empty()):
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

