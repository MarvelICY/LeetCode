#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Remove Duplicates from Sorted List II ] in LeetCode.

Created on: Nov 5, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        fast = head     
        slow = head
        #the distance between fast pointer and slow pointer remains as n
        for i in range(n):      
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        

#----------------------------SELF TEST----------------------------#

def main():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    n = 5
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    solution = Solution()
    head = solution.removeNthFromEnd(a,n)
    node = head
    while node is not None:
        print node.val
        node = node.next
            
if __name__ == '__main__': 
    main()