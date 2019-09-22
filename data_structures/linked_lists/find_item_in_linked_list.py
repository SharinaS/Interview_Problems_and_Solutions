#########################################################
# How to find an element in a Singly linked list
#########################################################
class NodeFinder(object):

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

def findNode(node):
    curr = node

    while curr is not None:
        if curr == node:
            return True
        curr = curr.next

    return False
print(findNode(b))
