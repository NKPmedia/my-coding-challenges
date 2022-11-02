""" 
Longest Repeating Character Replacement

Reference: https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Solution:
We want to come up with a solution such that for a given window, we want all
characters in a particular window to match the most common character in that
window.

Data Structure: Hash Table
Time Complexity: O(26 * n)
"""