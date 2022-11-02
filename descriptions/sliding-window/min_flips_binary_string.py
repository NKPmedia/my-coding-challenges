""" 
Minimum Number of Flips to Make the Binary String Alternating

Reference:
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

You are given a binary string s. You are allowed to perform two types of
operations on the string in any sequence: 

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s
becomes alternating. 

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Solution: the idea is a brute force solution but we can eliminate extra work by
using the sliding window approach. The time complexity is O(n) in the worst
case. However we can solve this using O(1) space using the sliding window
method below. 

Example: 111000

s = 111000111000
window:
    111000
    110001
    100011
    000111
    011100
    111000
    
TargetA: 101010
TargetB: 010101

Window 1:  111000
TargetA:   101010
Difference: 110010 = 3

Window 1:  111000
TargetA:   010101
Difference: 101101 = 3

Repeat for each window and keep track of the minimum difference.

# Reference: https://www.youtube.com/watch?v=MOeuK6gaC2A
"""