""" 
Graph Valid Tree

Reference:  https://www.lintcode.com/problem/178/#
Given a reference of a node in a connected undirected graph.

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to check whether these edges make up a
valid tree. 

Example: We want to visit each node and look at the neighbors of each node
recursively, until we've visited to every node connected to this input node.
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Solution: BFS
Time Complexity: O(n)

NOTE: A valid tree is a tree that has no cycles. 
"""