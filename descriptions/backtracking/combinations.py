""" 
Combinations

Reference: https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Note: we don't want duplicates in the solution.

Solution: Brute Force (backtracking)
Time Complexity: O(n^k); where k = height of tree 
"""