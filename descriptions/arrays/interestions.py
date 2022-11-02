"""
Intersection of Two Arrays II

Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note: Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.


Solution 1: Use a defaultdict
Time Complexity: O(n*m)

Solution 2: Use a counter 
Time Complexity: O(n)

Solution 3: Two pointers
Time Complexity: O(n + m)
"""