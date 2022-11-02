"""
Splitting a String Into Descending Consecutive Values

Reference:
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the
numerical values of the substrings are in descending order and the difference
between numerical values of every two adjacent substrings is equal to 1. 

Example: 
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.

Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Solution: Backtracking (brute force approach)
We check each possible path in the tree and see if any of the paths work out
where the difference between adjacent values is 1. So in some cases we wouldn't
continue on the DFS path, and thus by default are pruning the tree.
"""