
'''LINKED LISTS:
- contains nodes; each node consist of a value and a pointer to another node.
- starting node of a linked list is called a header
- a linked list is a chain of values connected with pointers, which makes it easy to add/remove items.
- saves memory - only allocates memory required for values to be stored during run-time (dynamic)
- linked list nodes can live anywhere in the memory (so, can be flexibly moved to another address)
- downside: has a linear lookup time - beginning to end is checked, so it can take up to n time to look for a value in a linked list. It also consumes lots of memory b/c of references (double linked lists waste even more memory b/c space has to be allocated for a back pointer)
- Linked lists are dynamic data structures (whereas arrays are not)
- Very efficient to add or remove item(s) in beginning - linear - unlike arrays which are O(n) when trying to add an item in the beginning (b/c the items must shift downstream).
- Less efficient to add item at end of linked list => have to traverse the list then update the references when we get there ==> O(n) / linear time complexity (versus it's very fast to insert items at end of an array)


RESOURCES:
- https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d
- Udemy's class: "Algorithms and Data Structures in Python"

######################

FROM UDEMY'S PYTHON FOR ALGORITHMS, DATA STRUCTURES AND INTERVIEW QUESTIONS: IMPLEMENTING A SINGLY LINKED LIST
 Remember, in a singly linked list, we have an ordered list of items as individual nodes that have pointers to other nodes.

 #######################

 Interview Questions regarding linked classes: Usually one will have to implement a node class, and use the various attributes and methods for that node class to solve the interview question.

 Note on O-time-complexity --> Linked lists have constant-time insertions and deletions in any position (awesome!), whereas arrays require O(n) time to do the same thing. Unfortunately, though, to access an element in a linked list, you need to take O(k) time to go from the head of the list to the kth element (boo!), while arrays have constant-time operations to access elements in an array.

'''
#########################################################
# Here's a class for a singly linked list (one only cares about the value and the nextnode in a singly linked list):
#########################################################
class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None # This is the next node the prior node points to.

# create instances of the class, aka, flesh out the linked list (note, though, that they won't be connected to each other, until the next step)
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# now, to link the nodes together:
a.next = b
b.next = c
c.next = d

# and, now, play with the node class
'''
print(a.value)
print(a.next.value)
print(b.next.value)
print(b.next)
print(c.next)
'''


#########################################################
# class for a doubly linked list
#########################################################

class DoublyLinkedListNode(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None
        self.priornode = None

a = DoublyLinkedListNode(10)
b = DoublyLinkedListNode(11)
c = DoublyLinkedListNode(12)

a.nextnode = b
b.nextnode = c
b.priornode = a
c.priornode = b
