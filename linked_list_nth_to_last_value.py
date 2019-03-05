'''Interview Style Problem proposed by a Udemy class titled, "Python for Data Structures and Interviews"

Problem Statement: Write a function that takes the head node of a singly linked list, and an integer value n, and then returns the nth to last node in the linked list. For example, if a linked list is [1,2,3,4], and 2 is n, the solution will return 4 in this case, because it's the second to last value of the list. If n is 3, it will return the 3rd from last value, which is 3.

Thought process: Because linked lists require us to progress from head to tail, we can create two variables that step through the list. Walk the first pointer n-steps from the head. The other pointer will start at the head. Then, both pointers step through the list, keeping n-spaces between them. When we get to the last node, which we know is the last because the last node points to None, we simple return the previous node.
'''
# Node class for testing function, nth_to_last:
class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

# function to solve the interview style problem:
def nth_to_last(n, head):
    curr = head
    prev = head

    for i in range(n-1):
        if curr.next == None: #edge case
            return "List is too short for the value you chose"
        curr = curr.next

    while curr.next:
        curr = curr.next
        prev = prev.next

    return prev.value

print(nth_to_last(3, a))
