'''
Reverse a linked list iteratively and then do it recursively.

How to do it, from LeetCode:
While you are traversing the list, change the current node's next pointer to point to its previous element. Since a node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. Remember to return the new head reference at the end.
'''


class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

def iterative_reversal(start_node):
    curr = start_node
    prev = None
    next = None


    while curr:
        next = curr.next # uses a variable to remember where the next box is, once the pointer from the original box and the next box is eliminated (in the next step)
        curr.next = prev # sets the pointer from the next box backwards to the original box.
        prev = curr # we set prev to be the original box
        curr = next # we set curr to be that variable from before, next, which is helping us move over to that next box - to the right.

    return prev.value
    #return prev # this is the line that leetcode needs

print(iterative_reversal(a))
'''Time complexity : O(n).
Space complexity : O(1)'''

############################################################################
''' RECURSIVE
From LeetCode:
The recursive version is slightly trickier and the key is to work backwards. Assume that the rest of the list had already been reversed, now how do I reverse the front part? Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø
Assume from node nk+1 to nm had been reversed and you are at node nk.
n1 → … → nk-1 → nk → nk+1 ← … ← nm
We want nk+1’s next node to point to nk.
So,
nk.next.next = nk;
Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it. This bug could be caught if you test your code with a linked list of size 2.

Time complexity : O(n)
Space complexity : O(n). The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.

'''

class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

def recursive(head):

    if not head.next:
        return head
    else:
        new_start = recursive(head.next)
        
    head.next.next = head
    head.next = None

    return new_start

print(recursive(a))
'''Runtime: 36 ms, faster than 25.25% of Python online submissions for Reverse Linked List.
Memory Usage: 16.5 MB, less than 9.48% of Python online submissions for Reverse Linked List.
'''
