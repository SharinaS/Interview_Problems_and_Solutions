'''LeetCode problem'''
###########################################################
'''
The Thought Process here:
All nodes but the head can be assigned to have a previous node. The head only has itself and the nodes that follow. Therefore, if a previous node exists, it is not the head node we're dealing with. If the pointer - which is going to move along the list step by step - finds a value that's supposed to be deleted, a temporary variable holds the value of the pointer during an if-else statement that differentiates if the pointer is at the head or at a regular node. Once the pointer is moved forward, a node points to one down the line, and if appropriate, the head is moved one node forward, then that temp node can then be deleted / it is set to None (good practice to remove it from memory). In sum, there's one while loop, there's an if/else statement showing the options of the pointer on a value to be deleted or not, and an inner if/else statement to show the options for the pointer being on the head or not (given the pointer is on a value to be deleted).
'''

# Node class so we can use it to test the function remove_linked_list_elements.
class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None # This is the next node the prior node points to.

# create instances of the class, aka, flesh out the linked list (note, though, that they won't be connected to each other, until the next step)
a = Node(6)
b = Node(2)
c = Node(6)
d = Node(4)
e = Node(5)
f = Node(6)

# now, to link the nodes together:
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# function that deletes each occurrence of a given value from the linked list:
def remove_linked_list_elements(head, val):
    pointer = head
    prev = None

    while pointer:
        if pointer.value == val:
            temp = pointer
            if prev: # as in, we are not at the head
                prev.next = pointer.next
                pointer = pointer.next # move to the next node
            else: # as in, we are at the head
                pointer = pointer.next
                head = pointer
            del temp
        else: # as in, pointer isn't at a value to be deleted
            prev = pointer # prev takes on the value of the pointer so pointer can move on to the next node
            pointer = pointer.next # move one node ahead

    # include when submitting code to leetcode:
    # return head

    # The following lets us check our answer by using class Node (don't include on leetcode answer):
    cur_node = head
    while cur_node:
        print(cur_node.value)
        cur_node = cur_node.next


remove_linked_list_elements(a,6)
