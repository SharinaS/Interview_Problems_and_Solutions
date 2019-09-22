'''IMPLEMENTATION OF A QUEUE, WITH A QUEUE CLASS, FROM UDEMY'S 'PYTHON FOR DATA STRUCTURES ALGORITHMS AND INTERVIEWS' CLASS:'''

# If the FRONT is considered to be the lowest index and the REAR is assigned to the highest index, do it this way (okayed by class professor and much preferred by me):
# front --> [0,1,2,3] <-- Rear

class Queue1(object):

    def __init__(self):
        self.items=[]

    def currentQueue(self):
        return self.items

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q1 = Queue1()
print(q1.size())
print(q1.isEmpty())
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.size())
print(q1.currentQueue())
print(q1.dequeue())
print(q1.currentQueue())



print(" ")

# If the FRONTis considered to be the highest index and the REAR is assigned to index 0, do it this way (class example):
# rear --> [3,2,1] <-- front

class Queue(object):

    def __init__(self):
        self.items=[]

    def currentQueue(self):
        return self.items

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item) #insert will insert the element at index 0, in this case, and shift the elements to the right.

    def dequeue(self):
        return self.items.pop() # item at the highest index value will be removed. dequeue() is defined as removing the front item and returning the item, therefore .pop() is appropriate, since it removes the item and returns the item.

    def size(self):
        return len(self.items)

q = Queue()
print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size())
print(q.currentQueue())
print(q.dequeue())
print(q.currentQueue())
