""" 
Product of Array Except Self

Reference: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Solution: Two pointers
Time Complexity: O(n)

# Build prefix table 
[1,2,3,4]
prefix: [1,2,6,24] -> 1*1 then 2*1 then 3*2 then 4*6; multiply by -1 to get the
postfix: [4,3,2,1] -> 4*1 then 3*4 then 2*12 then 1*24; and then reverse the order: [24,24,12,4]
"""