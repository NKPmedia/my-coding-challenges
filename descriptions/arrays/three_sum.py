""" 
Three Sum

Reference: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k]
== 0. 

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

Solution: Two pointers  
Time complexity: O(nlogn) + O(n^2) = O(n^2)
Space complexity: O(1) or O(n)

Reference: https://www.youtube.com/watch?v=jzZsG8n2R9A
"""