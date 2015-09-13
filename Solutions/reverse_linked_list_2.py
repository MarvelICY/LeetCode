#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Reverse Linked List II] in LeetCode.

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
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        for i in range(m-1):
            start = start.next
        start_prev = start      #start_prev indicate the last element before the sub list
        prev = start.next
        curr = start.next.next
        for j in range(n-m):    #curr is the second node in the sub list 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        start_prev.next.next = curr
        start_prev.next = prev     #now prev indicates the last element in the sub list
        return dummy.next




#----------------------------SELF TEST----------------------------#

def main():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    solution = Solution()
    head = solution.reverseBetween(a,2,3)
    node = head
    while node is not None:
        print node.val
        node = node.next
            
if __name__ == '__main__': 
    main()