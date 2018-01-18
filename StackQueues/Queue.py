class ArrayQueue:
    '''FIFO queue implementation using Python list as the underlying storage'''
    DEFAULT_CAPACITY = 10 #our default capacity set for our queue to help amortization

    def __init__(self):
        '''Create an empty queue
        We maintain the three variables:
        _data -> the list that holds the queue data
        _size -> the count of the current number of elements stored within the queue
        _front -> the current index that represents the front of the queue
        '''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        '''Returns the number of elements in the queue'''
        return len(self._data)

    def is_empty(self):
        '''Returns whether the queue is empty'''
        return self._size == 0

    def first(self):
        '''
        Returns but do not remove the first element in the queue
        Raise ValueError if the queue is empty
        '''

        if(self._size == 0):
            raise ValueError("Queue is currently empty.")

        return self._data[self._front]

    def dequeue(self):
        '''Returns AND remove the first element in the queue. Raise ValueError if empty'''
        if(self._size == 0):
            raise ValueError("Queue is currently empty.")
        frontValue = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) #our algorithm to keep track of the front of the queue: f = (f+1) % N
        self._size -= 1
        return frontValue

    def enqueue(self, e):
        '''Add element e to the end of the queue'''
        if(self._size == len(self._data)):
            self._resize(2 * len(self._data)) #resize the list if our queue has reached it's capacity

        avail = (self._front + self._size) % len(self._data) #our equation to find the first available index
        self._data[avail] = e
        self._size += 1

    def resize(self, c):
        '''resize our list to a capacity >= self._size'''
        old = self._data
        self._data = [None] * c
        start = self._front

        for i in range(self._size): #we only consider the existing elements
            self._data[i] = old[start] #intentially shift the indexes to the start
            start = (1 + start) % len(old) #use the size of the old list as the modular
        self._front = 0 #set the front to the first index



