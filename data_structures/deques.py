'''
Resources:
https://docs.python.org/3.7/library/collections.html#collections.deque

Syntax:
collections.deque([iterable[, maxlen]])
'''

#from collections import deque..........


# IMPLEMENTATION OF A DEQUE, WITH A DEQUE CLASS, FROM UDEMY'S 'PYTHON FOR DATA STRUCTURES ALGORITHMS AND INTERVIEWS' CLASS. When removing and adding items, be very attentive to knowing which end item was added to, and which end you're removing from. This may appear in interviews

class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
d.addFront('hello')
d.addRear('world')
print(d.size())
print(d.removeFront() + " " + d.removeRear())
print(d.isEmpty())
print(d.size())


print(" ")
# This too should be correct - it assumes that the front of the list called items is at the lowest index, while the rear is at the highest index. The reverse is true above.

class Deque2(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self,item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

d2 = Deque()
d2.addFront('hello')
d2.addRear('husband')
print(d2.size())
print(d2.removeFront() + " " + d2.removeRear())
print(d2.isEmpty())
print(d2.size())
