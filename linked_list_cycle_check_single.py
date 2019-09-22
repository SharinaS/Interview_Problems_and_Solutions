'''
From Udemy's "Python for Data Structures, Algorithms and Interviews"
Problem:
Given a singly linked list, write a function that takes in the first node in a singly linked list, and returns a boolean indicating if the linked list contains a "cycle." A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.

Coding Logic:
We can imagine that we have two runners on a track. If runner two is going fairly fast, eventually runner two will lap runner one. Thus, if runner two and runner one are never equivalent, there is no cycles within the linked list.
Therefore:
Write two markers that traverse through the list, marker1 and marker2. Have them both begin at node one of the list, and traverse through the linked list. Marker2 will move two nodes ahead for every one node that marker1 moves.
'''


class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

# instantiation of the class:
a = Node(1)
b = Node(2)
c = Node(3)

# linking the nodes together
a.nextnode = b
b.nextnode = c
c.nextnode = a

# check the linked list for the presence of cycle
def cycle_check(node):

    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.nextnode is not None: # we haven't reached tail, and marker2 isn't about to finish.
        marker1 = marker1.nextnode # this checks the next node
        marker2 = marker2.nextnode.nextnode # that is how we will make marker2 go faster than marker1.
        print(marker1.value, marker2.value)
        if marker2 is marker1:
            return True

    return False # otherwise, marker1 never met up with marker2, so there's no cycle present.

print(cycle_check(a))

##############################
# Submitted to Leetcode:

# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        marker1 = head
        marker2 = head

        while marker2 != None and marker2.next != None:
            marker1 = marker1.next
            marker2 = marker2.next.next

            if marker2 == marker1:
                return True

        return False
