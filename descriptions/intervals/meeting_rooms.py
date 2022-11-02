""" 
Minimum Meeting Rooms 

Reference: https://www.lintcode.com/problem/919/


Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

In other words, find the maximum number of non-overlapping meetings at any
point in time.

Example

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room

time complexity: O(nlogn)

Example diagram:
# 0======================30
# 	5====15
# 		 15=======25

Rearrange as: 
start = 0,5,15
end = 10,20,30 
"""