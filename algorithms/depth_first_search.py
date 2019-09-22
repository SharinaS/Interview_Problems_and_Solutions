'''
From Udemy's class called: "Algorithms and Data Structures in Python", taught by: Holczer Balazs
---> Graph traversal algorithm <---
BFS = breadth first search
DFS = Depth first search

DFS and BFS are both popular traversal algorithms. The difference between them is that --> BFS uses a queue while DFS USES A STACK. <---

Cocktail tidbit: DFS was considered for solving mazes in the 1800s.

About DFS:
It explores as far as possible along each branch before backtracking (in contrast, BFS is a layer-by-layer algorithm). Must be consistent: if you choose to visit the right subtree of the parent node, for all subtrees thereafter in the graph, you must start at the right subtree of the given node.

Time Complexity of DFS:
O(V+E), v is vertices, e is edges. Linear algorithm. This is the same complexity as BFS.

Memory Complexity of DFS:
Better than BFS!
We basically only have to store as many items, n, in the stack as the HEIGHT of the tree, which is log n! ==> The memory complexity is thus, O(log n) <==

Applications of DFS:
1) Topological ordering
2) Kosaraju algorithm for finding strongly connected components in a graph. Recommendation systems use the Kosaraju algorithm, like YouTube.
3) Detecting cycles (checking whether a graph is a DAG or not <-- DAG = directly acyclic graph. a directed graph is acyclic if it has topological ordering, or every edge goes from earlier in the order to later in the ordering. Checking for cycles important, b/c you can eliminate causes for a system freezing)
4) Generating mazes or finding way out of a maze

Note that an Iterative Deepening Depth First Search overcomes time wasting that can occur in DFS, when it dives down branches, when it just needs to get to a shallow node nearby.

Coding Options:
DFS can use Recursion or Iteration.
- Recursion is more compact. Note that in the background the operating system is going to use a stack abstract type, no matter if recursion or iteration is used.
- The recursive and iterative approaches are about the same as far as performance is concerned.


Pseudocode for Recursive Approach:
dfs(vertex)
    vertex set visited true
    print vertex

    for v in actual neighbors
        if v is not visited
            dfs(v)

'''
# Recursive DFS - usually the way to write DFS
# This is an Inorder Depth First Traversal
# See also data_structures/binary_trees.py
class Node(object):

    def __init__(self, value):
        self.value = value
        self.adjacencyList = []
        self.visited = False

class DepthFirstSearch(object):

    def dfs(self, node):
        node.visited = True
        print(node.value)

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)

# Build the tree
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

# initialize and call the code
dfs = DepthFirstSearch()
dfs.dfs(node1)

#       A
#      | \
#     B  C
#    |
#    D
#   |
#   E

##############################################
print(" ")
##############################################

'''Pseudocode for Iterative Approach: Uses LIFO structure: a Stack!
dfs(vertex)
    Stack stack
    vertex set visited true
    stack.push(vertex)

    while stack not empty
        curr = stack.pop()

        for v in actual neighbors
            if v is not visited
                v set visited true
                stack.push(v)'''

# Not recursion - using a stack to write a DFS algorithm:
class Nodal(object):

    def __init__(self, value):
        self.value = value
        self.adjacentList = []
        self.visited = False

class DepthFirstSearchIterative(object):

    def dfs(self, node):
        stack = []
        node.visited = True
        stack.append(node)

        while stack:
            curr = stack.pop()
            print(curr.value)

            for vertex in curr.adjacentList:
                if not vertex.visited:
                    stack.append(vertex)
                    vertex.visited = True

node1 = Nodal("A")
node2 = Nodal("B")
node3 = Nodal("C")
node4 = Nodal("D")
node5 = Nodal("E")
node6 = Nodal("X")
node7 = Nodal("Z")

node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node2.adjacentList.append(node4)
node4.adjacentList.append(node5)
node3.adjacentList.append(node6)
node3.adjacentList.append(node7)

dfs = DepthFirstSearchIterative()
dfs.dfs(node1)

#       A
#      | \
#     B  C
#    |  | \
#    D  X  Z
#   |
#   E
