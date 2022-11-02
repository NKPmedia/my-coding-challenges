""" 
Partition to K Equal Sum Subsets

Reference: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/


Given an integer array nums and an integer k, return true if it is possible to
divide this array into k non-empty subsets whose sums are all equal. 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

Solution: Backtracking
Time Complexity: O(k^n); k = k number of decisions, n = size of array

Slightly more efficient solution:
Time Complexity: O(k * 2^n); height of tree = n; k = k number of decisions (2);
so we have to find "k" number of subsets. In the next k subsets, we can't reuse
the numbers that was used in previous k subsets.
We determine if we include the number in our sum or not.

Reference: https://www.youtube.com/watch?v=mBk4I0X46oI 
"""