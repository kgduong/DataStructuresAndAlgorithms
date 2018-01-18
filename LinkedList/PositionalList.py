# implementing a positional linked list which gives positions to each node  of the linked list
from LinkedList import DoublyLinkedList


class PositionalList(DoublyLinkedList):
    '''Sequential container of elements allowing positional access'''

    class Position:
        '''An abstraction representing the location of a single element'''

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            '''Return the element stored at this position
            :return:
            '''
            return self._node._element

        def __eq__(self, other):
            '''Return True is other is a Position representing the same location.'''
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            '''Return True if other does not represent the same location'''
            return not (self == other)  # using negative of operator overload __eq__

    def _validate(self, p):
        '''Return position's node or raise appropriate error if invalid'''
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type.")
        if p._container is not self:
            raise ValueError('p does not belong to this PositionalList container.')
        if (p._next._node is None):
            raise ValueError('p is no longer valid')
        return p._node

    # This is our utility method to create Position instances
    def _make_position(self, node: object) -> object:
        '''Return Position instance for a given node(or None if sentinel)'''
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        '''Return the first Position in the list (None if empty)'''
        return self._make_position(self._header._next)

    def last(self):
        '''Return the last position in the list (None if empty)'''
        return self._make_position(self._trailer._prev)

    def before(self, p):
        '''Return the Position just before Position p (or None if p is first).'''
        node = self._validate(p)  # node with links to it's previous node
        return self._make_position(node._prev)  # get the position of the previous node

    def after(self, p):
        '''Return the Position just after Position p (or None if p is last)'''
        node = self._validate(p)
        return self._make_position(node._next)

    @property
    def __iter__(self):
        '''Generate a forward iteration of the elements of the list'''
        pos = self._first()
        while (pos is not None):
            yield pos.element()
            pos = self.after(pos)  # use our after function to iterate through the loop

    # ---------------------mutator------------------------------
    def _insert_between(self, e, predecessor, successor):
        '''Override the LinkedList version to return a position'''
        newest = super()._insert_between(e, predecessor,
                                         successor)  # super() keyword is used to call the base class function
        return self._make_position(newest)

    def add_first(self, e):
        '''Insert element e at the front of the list and return new position'''
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        '''Insert element e at the end of the list and return new Position'''
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p: Position, e):
        '''Insert element e into list before Position p and return new Position'''
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p: Position, e):
        '''Insert element e into the list after Position p and return the new Position'''
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p: Position):
        '''Remove and return the element at Position p'''
        node = self._validate(p)  # unpack the position to get it's node
        return self._delete_node(node)

    def replace(self, p: Position, e):
        '''Replace element at Position p with e
        Return the element formerly at Position p
        '''
        original = self._validate(p)
        old, original._element = original._element, e
        return old
