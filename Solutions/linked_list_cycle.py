#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Linked List Cycle] in LeetCode.

Created on: Nov 4, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        fast = head.next
        slow = head
        while fast.next is not None and fast.next.next is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False


#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()