""" 
K-sum Pairs in an Array
 
Reference: https://leetcode.com/problems/k-sum-pairs-in-an-array/

Given an array of integers nums and an integer k, return the number of unique k-sum pairs in the array.

A k-sum pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-sum pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-sum pairs in the array, (1, 2), (2, 3), (3, 4)
and (4, 5).

Solution: two pointers
Time complexity: O(n)
"""