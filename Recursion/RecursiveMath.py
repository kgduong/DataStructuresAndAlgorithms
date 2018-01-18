def recursive_reverse(S, start, stop):
    '''Reverse elements from s[start:stop]'''
    if start < stop - 1:
        S[start],S[stop-1] =S[stop-1],S[start]
        recursive_reverse(S, start+1, stop-1)

def iterative_reverse(S):
    '''Reverse elements of a sequence iteratively'''
    low = 0
    high = len(S)-1

    while(low<=high):
        if(low == high):
            return
        S[low],S[high] = S[high],S[low]
        low+=1
        high-=1

def recursive_power(x,n):
    '''compute x**n using recursion'''
    if(n == 1):
        return x
    return x * recursive_power(x,n-1)

def recursive_square_power(x,n):
    '''compute x** n using recursive squares and recursion'''
    if n == 0:
        return 1
    partial = recursive_square_power(x, n //2)
    result = partial*partial
    if(n%2 == 1):
        result *= x
        return result

def recursive_binary_sum(S,start,stop):
    '''Returns the sum of sequence S using recursion S[start:stop]'''
    if start >= stop: #stopping case
        return 0
    elif start == stop-1:
        return S[start] #if start is the middle of the binary split
    else:
        mid = (start+stop)//2#finds middle
        return recursive_binary_sum(S,start, mid) + recursive_binary_sum(S,mid,stop) #adds both halves

def recursive_max(S, index):
    '''Recursively find the max of the sequence'''
    if(index==0):
        return S[index]
    return max(S[index], recursive_max(S, index-1))

def recursive_min(S, index):
    '''Recursively find the min of a sequence'''
    if(index == 0):
        return S[index]
    return min(S[index], recursive_min(S, index-1))

def recursive_product(m,n):
    '''Uses recursion to find the product of two positive integers'''
    if(n <= 1):
        return m

    return m + recursive_product(m,n-1)

def recursive_subset(S): #[1,2], [2]
    '''Given a set S, recursively find all subset of S'''
    if(len(S) == 0):
        return [[]]
    head,tail = S[0], S[1:] #Get the first element and all of it's tail element
    subset_exclude_head = recursive_subset(tail)#Recurse for the tail elements
    subset_include_head = [([head] + subset) for subset in subset_exclude_head]#for the small subset then add the head element
    return subset_exclude_head + subset_include_head

def recursive_reverse_string(S,start,stop):
    '''A function that uses recursively reverses a string'''
    if(start>=stop-1):
        return S
    sequence = list(S)#convert S to list
    sequence[start],sequence[stop-1] = sequence[stop-1],sequence[start] #swap the elements
    S = ''.join(sequence)
    return recursive_reverse_string(S,start+1,stop-1)

def recursive_palindrone(S):
    '''A function that uses recursive_reverse_string to validate whether a string is palindrone'''
    lengthOfS = len(S)
    return S == recursive_reverse_string(S,0,lengthOfS)

def recursive_vowel_const(S,index):
    '''Recursively verifies if a string contains more vowels than consonants
        Implemented by recursively iterating through string and adding the const
    '''
    vowels = 'aeiouAEIOU'
    if (index == len(S)):
        return 0
    k = recursive_vowel_const(S, index+1)
    if(S[index] in vowels):
        return k + 1
    return k-1

def recursive_even_before_odd(S,start,stop):
    '''Need help with this'''
    while(S[start]%2 == 0):
        start += 1
    while(S[stop]%2 != 0):
        stop-=1
    if (start >= stop):
        return S
    S[start],S[stop] = S[stop],S[start]
    return recursive_even_before_odd(S,start,stop)


    return recursive_even_before_odd(S, index+1)

print(recursive_even_before_odd([1,3,2,4,4,4,5,5,5,2,2,3,4,5,6],0,14))




