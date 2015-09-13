#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Linked List Cycle II] in LeetCode.

Created on: Nov 5, 2014

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
    # take N is tha size of circle, 
    # K is distantance between the head and the beginning node of the circle
    # M is the distance between the first meet and the beginning node of the circle
    # first meeating of two pointers: slow = K + M ; fast = K + M + N 
    # as fast = 2*slow, we have N = K + M
    # set slow back to zero and the pace of both pointers as 1
    # when slow moves K, fast moves K to the beginning node and they meet again
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast == slow:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None


#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()