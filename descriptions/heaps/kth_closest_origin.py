""" 
K Closest Points to Origin

Reference: https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in). 

Example:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.

Solution : Min Heap -->  min heap contains k maximum
Complexity = K(logn); k = k closest points to origin
the size of the heap is n, where n is the number of points.

Note when "k" is small, Klog(n) < nlog(n)
"""