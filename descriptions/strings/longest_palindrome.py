""" 
Given a string s, return the longest palindromic substring in s.

Reference: https://leetcode.com/problems/longest-palindromic-substring/

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

Solution: iterate through the string and check to the left and right of each
character to see if the substring is a palindrome. 
Time Complexity: O(n^2)

Reference: https://www.youtube.com/watch?v=XYQecbcd6_c
"""