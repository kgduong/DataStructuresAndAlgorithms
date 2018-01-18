'''
File contains different implementations and applications of binary search and recursion. From recursive to iterative versions of binary search:
    Binary Search:
        T(n) = O(log n)
        S(n) = O(n)
'''

import os

def disk_usage(path):
    '''Returns the number of bytes used by a file/folder using recursion'''
    total = os.path.getsize(path)
    if(os.path.isdir(path)):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print( '{0:<7}'.format(total), path)
    return total

def binary_search(data, target, low, high):
    '''
    Return True if target is in data and limit high & low
    :param data:
    :param low: the lowest index for data
    :param high: the highest index for data
    :return:
    '''
    if(low > high):
        return False
    else:
        mid = (high + low)//2 # use "//" for floor division
        if(target == data[mid]):
            return True
        elif(target < data[mid]):
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

def recursive_fibonacci(n):
    '''Returns a pair of fibonacci numbers: (n, n-1)'''
    if(n<=1):
        return (n,0)
    else:
        (a,b) = recursive_fibonacci(n-1)
        return (a+b, a)

def iterative_binary_search(data,target):
    '''Implement binary search iteratively'''
    low = 0
    high = len(data) - 1

    while(low <= high):
        mid = (low+high)//2
        if(data[mid] == target):
            return True
        elif(data[mid] > target):
            high = mid - 1
        elif(data[mid] < target):
            low = mid + 1
    return False

