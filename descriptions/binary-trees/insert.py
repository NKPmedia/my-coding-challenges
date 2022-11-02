""""
Given a binary tree and a key, insert the key into the binary tree at the 
first position available:

Reference:
https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/

Original Tree
# 	   10
# 	  / \
# 	 11	  9
# 	/    / \
#    7    15  8 


Tree after insert 
# 	    10
# 	  /     \
# 	 11	     9
# 	/  \     / \
#    7   12   15  8 


The idea is to do iterative level order traversal of the given tree using queue. If we find a node whose left child is empty, we make new key as left child of the node. Else if we find a node whose right child is empty, we make the new key as right child. We keep traversing the tree until we find a node whose either left or right is empty. 
"""