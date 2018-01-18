import ctypes

class DynamicArray:
    '''A dynamic array class similar to the standard Python list class using the ctype array'''
    def __init__(self):
        '''Initialize an empty array'''
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        '''Returns a new array with capacity c'''
        return(c * ctypes.py_object)()

    def __len__(self):
        '''Returns number of elements stored within the array'''
        return self._n

    def __getitem__(self, k):
        '''return element at index k, or the negative index'''
        if not -self._n <= k <= self._n:
            raise IndexError("Invalid index.")
        elif(k >= 0):
           return self._A[k]
        elif(k < 0):
            return self._A[self._n+k]

    def append(self, obj):
        '''append a new object to the end of the array'''
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        '''Resize internal array to capacity c'''
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def insert(self, k, value):
        '''Insert value at index k and shifts list right'''
        if self._n == self._capacity: #in case of a resize, you can avoid the right shift
            B = self._make_array(2 * self._capacity)
            for j in range(k - 1):
                B[j] = self._A[j]
            B[k] = value
            for m in range(k+1, self._n):
                B[m] = self._A[m]
            self._n += 1
            self._capacity = 2 * self._capacity
            self._A = B
            return

        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1] #shift rightmost values
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        '''Remove the first occurrence of value or raise ValueError'''
        for j in range(self._n):
            if self._A[j] == value:
                for k in range(j, self._n - 1):
                    self._A[k] = self._A[k+1]
                self._A[self._n-1] = None  #set the last item of n to None
                self._n -= 1
                return
        raise ValueError("Value not found in the list")

    def pop(self):
        '''
        Removes the last element of the array and shrinks
        it's capacity if it falls under 1/4 capacity
        '''
        output, self._A[self._n - 1] = self._A[self._n - 1], None
        self._n -= 1
        if(self._n) <= self._capacity/4:
            self._resize(self._capacity // 2)
        return output






da = DynamicArray()
da.append(1)
da.append(2)
da.append(3)
da.append(3)
da.append(4)
da.append(5)
da.pop()
da.pop()
da.pop()
da.pop()
da.pop()
print(da)


