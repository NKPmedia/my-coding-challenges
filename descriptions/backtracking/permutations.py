""" 
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Reference: https://leetcode.com/problems/permutations/

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

Example: Each level is a sub-array:

                          [1,2,3]
                        /    |    \
                    [2,3]  [1,3]   [1,2]
                     /  \    /  \    /  \
                   [3] [2] [3] [1] [2]  [1]
                   
Remove value in each sub-array, and then add the value back to each sub-array
after we backtrack.
"""