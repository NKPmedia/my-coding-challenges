""" 
Find Largest Value in Each Tree Row

Reference: https://leetcode.com/problems/find-largest-value-in-each-tree-row/ 

Given the root of a binary tree, return an array of the largest value in each
row of the tree (0-indexed). 

Example: 
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

                1
              /   \
             3     2 
            / \     \
          5    3     9 


Solution: Breath First Search
Time Complexity: O(n) 
 """