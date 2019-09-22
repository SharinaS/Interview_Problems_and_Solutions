'''LeetCode Problem (medium)
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

Note - the following are not my solutions; had to explore other people's code to learn this concept.

==> See file "binary_trees.py in file "data structures" for more code on inorder traversal'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# RECURSIVE
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# ITERATIVE
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        trav = root
        res = []
        stack = []
        while stack or trav:
            while trav:
                stack.append(trav)
                trav = trav.left
            u = stack.pop()
            res.append(u.val)
            trav = u.right
        return res
