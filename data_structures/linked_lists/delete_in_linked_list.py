'''
From YouTube video by LucidProgramming, called Data Structures in Python: Singly Linked Lists - Deletion
(great video, by the way)
Goal: Given a key (data field), delete node with this field. Assume elements in linked list are unique. Consider that the node to be deleted could be the head, or it may not be the head - the head case is a bit of an edge case, so this needs to be accounted for. Following is a function for when a value is given, and for when a position is given.
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # for cases in which the data field is given
    def delete_node(self, key):
        cur_node = self.head
        # case 1 - if node to be deleted is head:
        if cur_node is not None and cur_node.value == key:
            # set head to the next node in the list:
            self.head = cur_node.next
            # get rid of the current element:
            cur_node = None

        # case 2 - node to be deleted is not the head node: Figure out what nodes are before and after the key node. Will need to keep track of the nodes just before and just after the current node we're on.
        prev_node = None
        while cur_node is not None and cur_node.value != key:
            prev_node = cur_node # keeps track of the previous node as we move through the list
            cur_node = cur_node.next
        if cur_node is None:
            return # element in list is not present, in other words
        prev_node.next = cur_node.next # points from the previous node to the node after the current node, so skips the current node.
        cur_node = None # removes the element from the list

    # for cases when the position is given, not the data field; assume the elements are unique and let's assume positions like index values in the linked list:
    def delete_node_at_position(self, position):
        cur_node = self.head
        # check if given position is the head of the list:
        if position == 0:
            self.head = cur_node.next # set the head to the next node in the list
            cur_node = None
            return

        # if position is not 0, then it's a node further down the list.
        prev_node = None
        count = 1 # not 0, since we've alredy taken care of this scenario

        while cur_node is not None and count != position:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None: # This means we reached the end of the list without finding the given position.
            return
        prev_node.next = cur_node.next
        cur_node = None



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.print_list()
print(" ")

llist.delete_node("B")
llist.print_list()
print(" ")

llist.delete_node_at_position(3)
llist.print_list()
