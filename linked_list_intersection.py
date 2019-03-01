'''
LeetCode Problem:
Write a program to find the node at which the intersection of two singly linked lists begins.
Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''
###############################################################################
'''
My thought process:
Use two pointers to step through each list, respectively. When each pointer reaches the end of it's list, have it then step through the other list, stopping only when the two pointers meet up. If there is an intersection, the pointers will meet up during their trips through the others' lists, because if one pointer got ahead of the other the first time, it is slowed down when it travels through the other pointers' list. The same goes for the other pointer - if it fell behind the first time, it will catch up when it steps through the other pointer's list.

Note, one can probably use a set. While progressing through headA, add to a set, and then compare with headB (this option not written out below)
'''

# A class so we can test the code in our code editor, such as Atom:
class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None # This is the next node the prior node points to.

# create instances of the class, aka, flesh out the linked list (note, though, that they won't be connected to each other, until the next step)
# headA
a = Node(4)
b = Node(1)
c = Node(8)
d = Node(4)
e = Node(5)

#headB
x = Node(5)
y = Node(0)
z = Node(1)

# now, to link the nodes together, and create the intersection (at value 8)
a.next = b
b.next = c
c.next = d
d.next = e

x.next = y
y.next = z
z.next = c


# Use a while loop that checks if the pointers are None or not:
def find_intersection(headA, headB):
    pointerA = headA
    pointerB = headB
    looped_twice = False

    while pointerA and pointerB:

        if pointerA is pointerB:
            return pointerA.value # remove the .value when submitting to LeetCode

        pointerA = pointerA.next
        pointerB = pointerB.next

        if pointerA is None and looped_twice == False:
            pointerA = headB
            looped_twice = True
        if pointerB is None:
            pointerB = headA

print(find_intersection(a, x))

#############################################################
# Another algorithm variation to solve the problem:
#############################################################
# Use a while loop that checks if the pointers are the same or not:
def find_intersection2(headA, headB):
    pointer1 = headA
    pointer2 = headB

    while pointer1 is not pointer2:
        if pointer1 is None:
            pointer1 = headB
        else: pointer1 = pointer1.next
        if pointer2 is None:
            pointer2 = headA
        else: pointer2 = pointer2.next
    return pointer1.value # remove the .value when submitting to LeetCode
print(find_intersection2(a,x))
