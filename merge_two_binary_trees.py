'''
From LeetCode:
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
      [1,3,2,4],[2,1,3,None,4,None,7]
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.

PROGRAMMING NOTE: NONE OF THE FOLLOWING SOLUTIONS ARE MINE. I'M STILL BAFFLED BY BINARY TREE CODE.
'''
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


##################################################

# recursive
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return None
        elif t2 == None:
            return t1
        elif t1 == None:
            return t2
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1




# iterative
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not (t1 != None and t2 != None):
            return t1 or t2
        else:
            stack = [(t1, t2, None, 0)]

            while stack:
                node1, node2, parent, left = stack.pop()
                if node1 and node2:
                    node1.val += node2.val
                    stack.append((node1.left, node2.left, node1, 1))
                    stack.append((node1.right, node2.right, node1, 0))
                elif node2:
                    if left:
                        parent.left = node2
                    else:
                        parent.right = node2
        return t1
