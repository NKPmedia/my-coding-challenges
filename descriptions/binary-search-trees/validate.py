"""
Binary Search Tree Validation

Reference: https://www.leetcode.com/problems/validate-binary-search-tree/

1.) Every node of the right subtree has to be larger than current node
2.) Every node on the left subtree is small than the current node
3.) All nodes on the left side of the tree must be less than root node

Solution: We know that the inorder traversal of a binary search tree gives a
sorted order of its elements -- so we will keep track of an array with each
nodes value and the check if final array is in ascending order. 

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
Input: 
			 8 
		    / \
		   3    10
		  / \	/ \
		 1	6  9  11

In order traversal = 1-3-6-8-9-10-11
So this would be a valid tree

Input:

			 5
			/ \
		   1   4
			  / \
			 3	 6

Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""