""" 
Maximum Length of a Concatenated String with Unique Characters

Reference:
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
Example 4:

Input: arr = ["aa","bb"]
Output: 0
Explanation: Both strings in arr do not have unique characters, thus there are
no valid concatenations.

Solution: if we did a brute force solution, we would have to check every
possible combination of strings. This time complexity would be O(n^2). We will
use backtracking as the solution.
Time Complexity: O(n^2)

Reference: https://www.youtube.com/watch?v=d4SPuvkaeoo
"""