'''
From Udemy's class called: "Algorithms and Data Structures in Python", taught by: Holczer Balazs

--> Dijkstra Algorithm <---
- a graph algorithm - shortest path algorithm - the fastest one known for arbitrary directed graphs with unbounded non-negative weights.
- can handle positive edge weights (the edge between 2 vertices must be > 0)
- It can find the shortest path from A to B; it can also construct a shortest path tree as well --> it defines the shortest paths from a source to all the other nodes.
- disadvantage: it must have a source; if the source moves, ie,  you move from Boston to Chicago , the data it collected from Boston to NY is no longer accessable, b/c you are viewing it from Chicago.
- asymptotically this is the fastest known single-source shortest-path algorithm for arbitrary directed graphs with unbounded non-negative weights.
- Time complexity: O(V*logV + E) if V is vertices and E is edges.
- It is a greedy algorithm, so on every iteration we want to find the minimum distance to the next vertex. Appropriate data structures are very important: Heaps (binary or fibonacci) or in general a priority queue. For the shortest path, we use minimum heaps; for the longest path, we use maximum paths.
'''
