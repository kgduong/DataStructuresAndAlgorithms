import collections
'''
A class meant to represent a a multidimensional vector, with operator overload applied to represent the class mathematically 
'''


class Vector:
    '''Represent a vector in a multidimensional space'''

    def __init__(self,d):
        '''Create d-dimensional vector of zeros'''
        if isinstance(d, collections.Sequence):
            coords = []
            for x in d:
                coords.append(x)
            self._coords = coords
        else:
            self._coords = [0] * d

    @property
    def __len__(self):
        '''Return the dimensions of the vector'''
        return len(self._coords)

    def __getitem__(self, j):#allows indexing: vector[j]
        ''''Return jth coordinate of vector.'''
        return self._coords[j]

    def __setitem__(self, j, value): #allows setting index: vector[j] = value
        '''Set jth coordinate of vector to value'''
        self._coords[j] = value

    def __add__(self,other):
        '''Return sum of two vectors or any sequence that supports __len__ and __getitem__'''
        if len(self) != len(other): #uses __len__ method
            raise ValueError("Dimensions of vector must agree")
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j] #uses __getitem__ method
        return result

    def __sub__(self, other):
        '''Return the subtraction of two vectors'''
        if len(self) != len(other):
            raise ValueError("Dimensions of vector must agree")
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        '''Return True if vector has same coordinate as other'''
        return self._coords == other._coords

    def __ne__(self, other):
        '''Returns True if vector does not have same coordinate as other'''
        return not self._coords == other._coords

    def __str__(self):
        '''Returns string representation of vector'''
        return '<' + str(self._coords)[1:-1] + '>' #create a list adaptation

    def __neg__(self):
        '''Returns the negative of a vector'''
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result

    def __mul__(self, other):
        if (type(other) == int or type(other) == float):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = other * self[i]
            return result
        else:
            if len(self) != len(other):
                raise ValueError("Dimensions of vector must agree")
            sum = 0
            for i in range(len(self)):
                sum += self[i] * other[i]
            return sum

    def __rmul__(self, other):
        if (type(other) == int or type(other) == float):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other[i]
            return result




v = Vector([1,2,3])



print(v)