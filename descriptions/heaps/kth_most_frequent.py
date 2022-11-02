""" 
Top K Most Frequent Elements

Reference: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Solution1: Counter
Time Complexity: O(n)

Solution2: Max Heap
Time Complexity: O(nlogk); where n = len(nums) and k = k.
"""