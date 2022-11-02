"""
Max Contiguous Subarray Sum

Reference: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum. 

Example: 
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

Solution: basically a sliding window approach where we remove negative prefixes
from the contiguous subarray and keep track of the maximum sum. 
We can minimize the number computations by using previous subarrays sum and
then increment by one index to create the next subarray and then just take the
max between the two. 
Time Complexity: O(n)

Reference: https://www.youtube.com/watch?v=5WZl3MMT0Eg
"""