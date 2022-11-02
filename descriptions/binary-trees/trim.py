""" 
Trim a Binary Search Tree

Reference: https://leetcode.com/problems/trim-a-binary-search-tree/

Given the root of a binary search tree and the lowest and highest boundaries as
low and high, trim the tree so that all its elements lies in [low, high].
Trimming the tree should not change the relative structure of the elements that
will remain in the tree (i.e., any node's descendant should remain a
descendant). It can be proven that there is a unique answer. 

Return the root of the trimmed binary search tree. Note that the root may
change depending on the given bounds.

Example:
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Solution: Recursion DFS
Time Complexity: O(n)
Memory Complexity: O(h) -> where h = height of tree
"""