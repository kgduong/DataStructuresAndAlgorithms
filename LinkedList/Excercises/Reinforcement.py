from LinkedList.DoublyLinkedList import DoublyLinkedList

def recursiveCount(node): #node input should be the head of the list
    if(node._next == None and node.prev == None and node._element == None):
        return 0 #empty list
    return 1 + recursiveCount(node._next)

def findMiddle(doublyLinkedList):
    head = doublyLinkedList._header
    tail = doublyLinkedList._trailer
    while (head != tail):
        if head._next is tail:
            return head
        if head._next is tail._prev:
            return head._next
        head = head._next
        tail = tail._prev


dll = DoublyLinkedList()
node1 = dll._insert_between(1, dll._header, dll._trailer)
node2 = dll._insert_between(2, node1, dll._trailer)
#node3 = dll._insert_between(3, node2, dll._trailer)

e = findMiddle(dll)
print(e._element)