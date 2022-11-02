""" 
Word Search

Reference: https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Solution: Backtracking with DFS
Time Complexity: O(n * m * dfs); dfs = len(word) * 4 ^ len(word); 4^n 
O (n * m * 4^n)

We will look at every cell in the grid and check the neighbors
to see if we can construct the word. 

Reference: https://www.youtube.com/watch?v=pfiQ_PS1g8E&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=1
"""