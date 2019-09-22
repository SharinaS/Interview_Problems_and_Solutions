'''
From YouTube video by LucidProgramming, called Data Structures in Python: Singly Linked Lists - Insertion
(great video, by the way)
'''

class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None # This is the next node the prior node points to.


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def append(self, value): # appends node to end of list
        # if the list is totally empty
        new_node = Node(value) #use node class to define a new node. It has the data from our append function

        # check if list is empty - check if head has no component
        if self.head is None: # as in, there are not yet nodes in the list
            self.head = new_node
            return

        # for lists that are already establihed, let's put a node at the end:
        last_node = self.head # it will initially be equiv to the head, but it will move through the list so it ends up as the last node
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, value): # adds node to beginning of list
        new_node = Node(value)
        new_node.next = self.head #points from the new_node to the current head
        self.head = new_node # changes the official head to the new first node, which is our new_node.

    def insert_after_node(self, prev_node, value): # add node to within the list
        # check if node we want to insert after is in list
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(value)
        # make new node point to the node in the list that should go after it:
        new_node.next = prev_node.next
        # make node that is supposed to go before new_node to point to new node:
        prev_node.next = new_node


llist = LinkedList()
llist.append("e")
llist.append("f")
llist.append("g")
llist.append("h")
llist.prepend("d")
#print(llist.head.value)
#print(llist.head.next.value)

llist.insert_after_node(llist.head.next, "Z")

llist.print_list()
