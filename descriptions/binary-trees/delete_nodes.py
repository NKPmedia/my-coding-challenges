""" 
Delete Nodes And Return Forest


Reference: https://leetcode.com/problems/delete-nodes-and-return-forest/
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.


Example 1:

#                      1
#                    /   \
#                   2      3
#                  / \    / \
#                 4   5   6  7 
                 
Output:                 1
 #                   /     \
 #                  2       NA
 #                 / \     /  \
 #                4  NA   6    7 


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

Solution: Depth First Search
Time Complexity: O(n)
Memory Complexity: O(n + h); where h = height of the tree 

NOTE: A node which does not have any parents is considered as root. So in the
example above, 1,6,7 are considered as roots. 

Check Two Conditions:
root.val is in to_delete or not. 
We need to keep track of the parent of the node as well. 


ToDo: not entirely working as expected. Need to fix it to handle disjoint trees.
"""