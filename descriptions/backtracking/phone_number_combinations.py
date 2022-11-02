""" 
Letter Combinations of a Phone Number

Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/


Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order. Note that 1 does not map to any letters.

Example:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "2"
Output: ["a","b","c"]

Solution: dfs
Time complexity: O(n*4^n)
4^n is the number of possible combinations
"""