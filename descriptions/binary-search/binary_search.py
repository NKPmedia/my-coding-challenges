"""
Binary Search

Reference: https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1. 

Note: You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Steps:
    - Compare x with the middle element.
    - If x matches with the middle element, we return the mid index.
    - Else if x is greater than the mid element, 
        - Then x can only lie in the right (greater) half subarray after the mid element. 
        - Then we apply the algorithm again for the right half.
    - Else if x is smaller, the target x must lie in the left (lower) half. 
        - So we apply the algorithm for the left half.
"""