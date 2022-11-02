"""
Rotate Array

Reference: https://leetcode.com/problems/rotate-array/ 

Given an array, rotate the array to the right by k steps, where k is
non-negative. 

Example:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Solution:
Time Complexity: O(n) -> Modify in place
Memory Complexity: O(1)

Note: 

k = 2 
x = [1,2,3,4,5]

|  |  | 1 | 2 | 3 | 

when moving an element to the right and it's outside the length of the
array (e.g. 4 & 5), we can use (i + k) % len(nums) to position the element at
the correct index. 

Example: i = 4; (3 + 2) % 5 = index = 0
Example: i = 5; (4 + 2) % 5 = index = 1
"""