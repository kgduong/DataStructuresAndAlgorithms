from StackQueues.Stack import ArrayStack

def transfer(s : ArrayStack, t : ArrayStack):
    '''Transfer all element from Stack S onto stack T'''
    while (s.is_empty() != True):
        e=s.pop()
        t.push(e)
    return t

def recursive_empty_stack(s : ArrayStack):
    '''Recursively empty a stack'''
    if(s.is_empty()):
        return
    print(s.pop())
    return recursive_empty_stack(s)

