# IMPLEMENTATION OF A STACK, WITH A STACK CLASS, FROM UDEMY'S 'PYTHON FOR DATA STRUCTURES ALGORITHMS AND INTERVIEWS' CLASS:

class Stack(object):

    def __init__(self):
        self.items = [] #base off the Stack

    def isEmpty(self):
        return self.items == [] # once items are pushed on the list, this function will return false

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        #return self.items[len(self.items)-1] #returns last item that was put in
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push('pears')
s.push('apples')
s.push(2)
print(s.peek())
s.pop()
print(s.peek())


print(s.isEmpty())
