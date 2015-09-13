#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Remove Nth Node From End of List] in LeetCode.

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
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        start = head
        end = head.next
        while end is not None:
            if start.val != end.val:    #skip nodes with different values
                if end.next == None:
                    return dummy.next
                else:
                    prev = prev.next
                    start = prev.next
                    end = start.next
            if start.val == end.val:    #record the starting node of same nodes
                if end.next == None:
                    prev.next = None
                    return dummy.next
                elif end.val != end.next.val:   #remove the duplicated nodes
                    prev.next = end.next
                    start = end.next
                    end = end.next.next
                else:
                    end = end.next     #scale the length of the diplicated nodes
        return dummy.next


#----------------------------SELF TEST----------------------------#

def main():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(3)
    a.next = b
    #b.next = c
    c.next = d
    d.next = e
    solution = Solution()
    head = solution.deleteDuplicates(a)
    node = head
    while node is not None:
        print node.val
        node = node.next
            
if __name__ == '__main__': 
    main()