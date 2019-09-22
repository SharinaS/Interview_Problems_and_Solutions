'''
From Udemy's class called: "Algorithms and Data Structures in Python", taught by: Holczer Balazs
---> Graph traversal algorithm <---
BFS = breadth first search
DFS = Depth first search

BFS is an algorithm to traverse or search in data structures like a tree or graph. The algorithm starts with a root node and visits the node itself first. Then it traverses its neighbors, traverses its second level neighbors, traverses its third level neighbors and so on. When we do BFS in a tree, the order of the nodes we visited is in level order; Level-Order Traversal. -- From LeetCode (https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/990/)

Behavior: The search direction is reversed at each level (https://towardsdatascience.com/top-algorithms-and-data-structures-you-really-need-to-know-ab9a2a91c7b5)

LEVEL-ORDER TRAVERSAL is breadth-first traversal for a tree.

It's a common interview question to ask:
For a BFS, we can use a queue... for a DFS, we can use a stack, BUT, usually we implement it with recursion (under the hood of recursion though, we use the stack, so it's really a stack regardless).

RUNTIME COMPLEXITY:
... is linear because we visit each node exactly once: O(V+E), where V is the number of vertexes or nodes, and E is the number of edges in the graph.

MEMORY COMPLEXITY:
Not good - we store lots of references when using this algorithm. Depth-first search is usually preferred if memory is an issue.
Memory is O(n), if we want to traverse a tree that contains n items.

STRENGTHS:
1) It constructs the shortest path. Dijkstra Algorithm does a BFS if all the edge weights are equal to 1. Very important in maximum flow algorithms: Edmonds-Karp algorithm uses BFS for finding augmenting paths.
2) AI algorithms / machine learning - robots can discover the surroundings more easily with BFS than DFS, as in robot movements. BFS is going to discover the local environment b/c it goes layer by layer.
3) Garbage collection - Cheyen's algorithm helps to maintain active references on the heap memory. It uses BFS to detect all the references on the heap, and if there are dead references, it gets rid of them.
4) Serialization / deserialization of tree-like structure - for when order does matter. It allows the tree to be reconstructed in an efficient manner.

Remember, leaf nodes are those that do not have children.

STRUCTURE:
Use a FIFO (first-in, first-out) structure. A queue! That's why we use the queue data type.
Basic idea: We visit a vertex on a row by row basis, considering the vertexes in a local environment. We have an empty queue at the beginning and we keep checking whether we have visited the given node or not. Keep iterating until queue is not empty. The size of the queue will keep changing, since once we enter the while loop, we remove an element, then add its children.

PSEUDOCODE:
(note that we cannot implement BFS in a recursive manner, while DFS can be implemented recursively)

bfs(vertex)
    Queue queue
    vertex set visited true # so we don't visit this node over and over again.
    queue.engueue(vertex)

    while queue not empty
        actual = queue.dequeue() # remove the starting vertex so we can process its children. FIFO.

        for v in actual neighbors # sometimes neighbors are called children. visit all the children of the vertex in question.
            if v is not visited
                v set visited true
                queue.enqueue(v)


          A
         / \
        B   C
       /   / \
      D   E  F
     /
    G

'''
# From Udemy's class called: "Algorithms and Data Structures in Python", taught by: Holczer Balazs
class Node(object):

    def __init__(self, value):
        self.value = value
        self.adjacencyList = [] # allows us to build the graph of vertices and edges.
        self.visited = False # checks if we have visited a node or not

class BreadthFirstSearth(object):

    def bfs(self, startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:

            curr = queue.pop(0) # we get the first item we have inserted
            print(curr.value)

            for vertex in curr.adjacencyList: # we visit the neighbors of that current node with the help of the adjacency list.
                if not vertex.visited:
                    vertex.visited = True
                    queue.append(vertex)

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node3.adjacencyList.append(node5)
node3.adjacencyList.append(node6)
node4.adjacencyList.append(node7)

bfs = BreadthFirstSearth() # instantiate the class
bfs.bfs(node1) # call the bfs.bfs method and specify the starting node

################################################################################
print(" ")
################################################################################
# Another way to look at the same type of algorithm, using a queue / iterative method to create a level-order-traversal, from Geeks for Geeks: https://www.geeksforgeeks.org/level-order-tree-traversal/
# For each node, first the node is visited and then it’s child nodes are put in a FIFO queue.

class Node:
    # utility function to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Iterative method to print the height of the binary tree
def LevelOrder(root):
    # base case
    if root is None:
        return

    # create empty queue for level order traversal
    queue = []

    # Enqueue root and initialize height
    queue.append(root)

    while len(queue) > 0:
        # print front of queue and remove it from queue
        print(queue[0].value)
        node = queue.pop(0) # node is an iterator object

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # enqueue right child
        if node.right is not None:
            queue.append(node.right)

# Driver program
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.right.left = Node('E')
root.right.right = Node('F')
root.left.left.left = Node('G')

print("Level Order Traversal of binary tree is")
LevelOrder(root)
