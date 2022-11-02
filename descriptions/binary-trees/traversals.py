"""
Pre-order, In-order, and Post-order Traversals:

Reference: https://www.youtube.com/watch?v=6oL-0TdVy28

Example tree:
         _10_
        /     \
       7       11
     /  \        \
    6    8       20
   /      \     /   \
   1      9    14   22
    
- Pre-order:  [10, 7, 6, 1, 8, 9, 11, 20, 14, 22] --> Root -> Left -> Right
- In-order:   [1, 6, 7, 8, 9, 10, 11, 14, 20, 22] --> Left -> Root -> Right
- Post-order: [1, 6, 9, 8, 7, 14, 22, 20, 11, 10]

Example:

preorder: 1-2-4-5-3-6-7
inorder:  4-2-5-1-6-3-7
postorder: 4-2-5-6-3-7-1
levelorder: 1-2-3-4-5-6-7
         1
        /  \
       2     3
     /  \   /  \
    4   5   6   7
"""