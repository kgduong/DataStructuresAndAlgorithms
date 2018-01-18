#A circularQueue implemented with the use of a LinkedList

class CircularQueue:
    '''Queue implementation using circularly linked list for storage'''

    class _Node:
        '''Lightweight nonpublic class for storing a singly linked node.'''
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
       '''Create an empty queue'''
       self._tail = None
       self._size = 0

    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size

    def is_empty(self):
        '''Returns whether or not the queue is currently empty'''
        return self._size == 0

    def first(self):
        '''Returns (but do not remove) the element at the front of queue

        Raise empty exception if the queue is empty.
        '''

        if(self.is_empty()):
            raise ValueError("The queue is currently empty.")
        head = self._tail._next #first element is always pointed by our tail element
        return head._element

    def dequeue(self):
        '''Remove and return the first element of the queue(FIFO)

        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise ValueError("The queue is currently empty.")

        oldhead = self._tail._next
        if(self._size == 1):
            self._tail = None
        else:
            self._tail._next = oldhead._next

        self._size -= 1

    def enqueue(self, e):
        '''Add an element to the back of the queue'''
        newest = self._Node(e, None)
        if(self.is_empty()):
            newest._next = newest #Circulary link node to itself
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        '''Rotate front element to the back of the queue'''
        if(self._size > 0):
            self._tail = self._tail._next #old head becomes new tail


