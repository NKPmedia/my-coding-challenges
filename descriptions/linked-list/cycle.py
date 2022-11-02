""" 
Linked List Cycle

Reference: https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter. 

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to
the 1st node (0-indexed).

3 ---> 2 ---> 0 ---> -4 
       ^              |
       |              |
       <------------- 
                      
Solution: Floyd's Cycle-Finding Algorithm; we can use two pointers, slow and
fast. Slow will increment by 1 and fast will increment by 2.

NOTE: if there is a cycle, the fast pointer will eventually meet the slow
pointer and thus a cycle exists.

Time Complexity: O(n)
"""