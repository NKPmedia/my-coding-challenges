""" 
Non-overlapping Intervals

Reference: https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Solution: 
If we did a brute for approach, we would have to check every interval
and determine if it overlaps with any other interval. This would be O(n^2).

We can implement an Greedy approach to solve this problem and be more
efficient. The time complexity for the below solution is O(nlogn).

Example Diagram (sorted by starting element):
1=====2
      2=====3
            3=====4
1===========3

Sort the first index of the intervals 
[1,2],[1,3],[2,3],[3,4]


Edge Case: 
   =================== --> remove this interval 
============= ===========

Edge Case:
  ======= --> remove this interval
=========== ===========
"""