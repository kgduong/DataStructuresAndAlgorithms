from LinkedList.DoublyLinkedList import DoublyLinkedList
#An implementation of a doubly linked deque using our DoublyLinkedList as a base class

class LinkedDeque(DoublyLinkedList):
    '''Doubly-ended queue implementation based on a doubly linked list'''

    def first(self):
        '''Return but do not remove the element at the front of the queue'''
        if self.is_empty():
            raise ValueError("The Deque is currently empty.")
        return self._header._next._element

    def last(self):
        '''Return but do not remove the element at the back of the queue'''
        if self.is_empty():
            raise ValueError("The Deque is currently empty.")
        return self._trailer._prev._element

    def insert_first(self, e):
        '''Add an element to the front of the queue'''
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        '''Add an element to the back of the queue'''
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        '''Remove and return the element from the front of deque

        Raise exception if the deque is empty
        '''
        if(self.is_empty()):
            raise ValueError("The Deque is currently empty.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        '''Remove and return the last element of the deque

        Raise exception if the deque is empty.
        '''
        if(self.is_empty()):
            raise ValueError("The Deque is currently empty.")
        return self._delete_node(self._trailer._prev)

    
