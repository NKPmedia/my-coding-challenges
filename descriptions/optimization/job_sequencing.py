""" 
Job Sequencing with Deadlines

Reference: https://www.geeksforgeeks.org/job-sequencing-problem/

Given an array of jobs where every job has a deadline and associated profit if
the job is finished before the deadline. It is also given that every job takes
a single unit of time, so the minimum possible deadline for any job is 1

The goal is for the job to complete within the deadline such that the profit is
maximized. Assume each job takes 1 unit of time to complete. 

Constraints: job must be completed within the deadline.

Example:
inputs:
n_jobs = 5
deadlines = [2, 2, 1, 3, 3]
profits - [20, 15, 10, 5, 1]

Solution: Greedy Algorithm
Time Complexity: O(n^2)
"""