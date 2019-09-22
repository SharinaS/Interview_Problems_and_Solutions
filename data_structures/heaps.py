'''
From Udemy's class called: "Algorithms and Data Structures in Python", taught by: Holczer Balazs

HEAP
- basically a binary tree
- Two types: minimum and maximum heaps
- In a max heap, the keys of parent nodes are always >= to those of the children. The highest key is in the root node.
- In a min heap, the keys of parent nodes are always <= to those of the children. The lowest key is in the root node.
- It is complete --> it cannot be unbalanced. We insert every new item to the next available place.
- Applications: Dijkstra's Algorithm, Prims Algorithm
- The heap is one maximally efficient implementation of a priority queue abstract data type.
- The heap has nothing to do with the pool of memory from which dynamically allocated memory is allocated.

HEAP PROPERTIES:
- It is complete. No matter what, there will be a left and a right child for each node. They are constructed on a line by line basis from left to right. There is no missing node from left to right in a layer.
- In a binary heap every node can have 2 children, left child and right. Unlike a binary tree, the left is not smaller or greater than a parent; the children don't have anything to do with each other. What's important is that the parent is smaller or bigger, depending on whether it's a min or max heap.
- Min heap - the parent is always smaller than the value of the children. Used to find minimum distance. Root node will be the smallest node of all the nodes. Parent node will always be smaller than a child node.
- max heap - the parent is always bigger than the values of the children. Used to find maximum distance. The parent node will be the biggest value of the other nodes.
- Accessed via O(1) time complexity
'''
