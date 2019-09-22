# If we don't know how many nodes there are, given the head variable, write a function that returns the number of nodes in the linked list
class Node(object):

    def __init__ (self, value):
        self.data = value
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

def countNodes(head):
    counter = 1 # keeps track of how many nodes seen so far
    current_node = head # keeps track of which node we're looking at

    while current_node.next is not None:
        current_node = current_node.next
        counter += 1

    return counter

print(countNodes(a))
