'''
INORDER AND PREORDER ON BINARY TREES
- LeetCode - some of the following is designed to run on LeetCode's pages. See also Algorithms file on depth_first_search.
Resources:
- Geeks for Geeks - https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

'''

#Simple example of accessing values from the nodes from a Binary Tree:
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Tree()
root.data = "rooty"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

#print(root.left.data)

################################################################################
# geeksforgeeks printable function for doing inorder, postorder, preorder tree traversal
################################################################################
'''
INORDER TRAVERSAL of a nodes' values, given a binary tree
1. Traverse the left subtree, ie, call Inorder(left-subtree)
2. Visit the root
3. Traverse the right subtree, ie, call Inorder(right-subtree)

      1
     /  \
    2    3
   / \   /\
  4  5  6  7
 /\  /
8  9 10
Inorder traversal for the above figure is (left root right): 8 4 9 2 10 5 1 6 3 7


PREORDER TRAVERSAL of a binary tree. Used to create a copy of the tree. Also helpful to get "prefix expression on an expression tree" (look this up at some point).

1. Visit the root
2. Traverse the left subtree, ie, call Preorder(left-subtree)
3. Traverse the right subtree, ie, call Preorder(right-subtree)

      1
     /  \
    2    3
   / \   /\
  4  5  6  7
 /\  /
8  9 10
Preorder traversal for the above figure is (root left right): 1 2 4 8 9 5 10 3 6 7


POSTORDER TRAVERSAL is used to delete the tree. Also helpful to get the postfix expression of an expression tree (look up later).

1. Traverse the left subtree, ie, call Postorder(left-subtree)
2. Traverse the right subtree, ie, call Postorder(right-subtree)
3. Visit the root

      1
     /  \
    2    3
   / \   /\
  4  5  6  7
 /\  /
8  9 10
Postorder traversal for the above figure is (left right root): 8 9 4 10 5 2 6 7 3 1

LEVEL ORDER TRAVERSAL is breadth first traversal for the tree (see file algorithms/breadth_first_search.py)
Time complexity for using a queue is 0(n) where n is number of nodes in the binary tree.
1. First the node is visited
2. Child nodes are put in a FIFO queue
'''

# Note - Recursion is one of the most powerful and frequent used methods for solving tree related problems (LeetCode)

class Node:
    def __init__(self, val):
        self.left = None
        self.right= None
        self.val = val

def inorder(root):
    if root:
        # first recur on left child
        inorder(root.left)
        #then print data of node
        print(root.val)
        #then recur on right child
        inorder(root.right)

def preorder(root):
    if root:
        # first print the data of the node
        print(root.val)
        # then recur on left child
        preorder(root.left)
        # then recur on right child
        preorder(root.right)

def postorder(root):
    if root:
        # first recur on left child
        postorder(root.left)
        # then recur on right child
        postorder(root.right)
        # then print the node data
        print(root.val)

# Using a queue (see commented code in breadth_first_search file in Algorithms file):
def levelorder(root):
    if root:
        queue = []
        queue.append(root)

        while len(queue) > 0:
            print(queue[0].val)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def levelorder_level_by_level(root):
    ''' note: append each level to temp queue, then have that list appended into queue, so output is a list of lists. This version iterates through the nodes of each level, keeping track within each loop of what the current level nodes are, and what the next level nodes will be. Note: Does not use a queue. Beats 99.98% of Python submissions. '''

    if root:

        result = []
        current_level = [root]

        while current_level:
            values = []
            new_level = []

            for node in current_level:
                values.append(node.val)

                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            result.append(values)
            current_level = new_level

        return result


def levelorder_level_by_level_using_queue(root):
    '''2 biggest lessons here was (1) to not be afraid to use many lists to keep track of levels and to allow for refresh of variable in the while loop, and (2) to make sure to know if the program needs to check to see if something exists or not. When the last 2 if statements are not added, the while loop goes to infinity, b/c no where else do we check if the curr_value or next_level even exist. We also had to check if the node existed within the for loop.'''

    result = []
    # nodes at the level we're working with
    level = [[root]]

    while level:
        # values of the nodes at the level we're working with, to then be appended to the result as integers.
        curr_value = []
        # keeps track of the next level nodes; will become the list called level, so they can be popped off the 2d list and iterated through.
        next_level = []

        curr_level = level.pop()

        for node in curr_level:
            if node:
                curr_value.append(node.val)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if curr_value:
            result.append(curr_value)
        if next_level:
            level.append(next_level)

    return result


# This takes 24 ms to run, faster than 99.98% of python submissions on Leetcode. Uses 12.2 mb, though, less than 5.04% of python online submissions on leetcode.
def levelorder_level_by_level_using_queue2(root):
    '''Make sure to check what lines of code really need to be validated with an if statement'''
    if root:
        result = []
        level = [[root]]

        while level:
            curr_value = []
            next_level = []

            curr_level = level.pop()

            for node in curr_level:
                curr_value.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if curr_value:
                result.append(curr_value)
            if next_level:
                level.append(next_level)

        return result

'''
      1
     /  \
    2    3
   / \   /\
  4  5  6  7
 /\  /
8  9 10
'''



# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)

print("Inorder traversal of binary tree is")
inorder(root)

print("Preorder traversal of binary tree is")
preorder(root)

print("Postorder traversal of binary tree is")
postorder(root)

print("Levelorder traversal of binary tree is")
levelorder(root)

print("level order traversal of binary tree with each level assigned to a list:")
print(levelorder_level_by_level(root))

print("levelorder_level_by_level_using_queue2:")
print(levelorder_level_by_level_using_queue2(root))


################################################################################
# LeetCode solution for Inorder Tree Traversal
################################################################################


# Code found on LeetCode and submitted to Leetcode.
class TreeNode:
    """ definition for a binary tree node """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_recursive:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # left root right
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # root left right
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # left right root
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

class Solution_iterative:
    """ iterative inorder traversal solution (left root right) """
    def inorderTrav(root):
        result = []
        stack = []

        while (root != None) or (stack != []):
            #Iterate through the root, append the root to the stack / go through left tree
            while (root != None):
                stack.append(root)
                root = root.left
            #Pop the first root...,append the result to the result
            root = stack.pop()
            result.append(root.val)
            #Go now to the right side
            root = root.right

        return result
