#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Reverse Nodes in k-Group] in LeetCode.

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
    # @param k, an integer
    # @return a ListNode
    # copy
    def reverse(self, start, end):
        newhead = ListNode(0) 
        newhead.next = start
        while newhead.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = newhead.next
            newhead.next = tmp
        return [end, start]
    def reverseKGroup(self, head, k):
        if head == None: return None
        nhead = ListNode(0)
        nhead.next = head
        start = nhead
        while start.next:
            end = start
            for i in range(k-1):
                end = end.next
                if end.next == None: return nhead.next
            res = self.reverse(start.next, end.next)
            start.next = res[0]
            start = res[1]
        return nhead.next


#----------------------------SELF TEST----------------------------#

def main():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    k = 2
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    solution = Solution()
    head = solution.reverseKGroup(a,k)
    node = head
    while node is not None:
        print node.val
        node = node.next
            
if __name__ == '__main__': 
    main()