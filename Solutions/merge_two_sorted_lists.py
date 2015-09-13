#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Merge Two Sorted Lists] in LeetCode.

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
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        node = dummy
        node_l1 = l1
        node_l2 = l2
        while node_l1 != None and node_l2 != None:
            if node_l1.val < node_l2.val:

                node.next = node_l1
                node = node.next
                node_l1 = node_l1.next
            else:
                node.next = node_l2
                node = node.next
                node_l2 = node_l2.next

        if node_l1 == None:
            node.next = node_l2

        if node_l2 == None:
            node.next = node_l1

        return dummy.next


#----------------------------SELF TEST----------------------------#

def main():
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(5)
    d = ListNode(7)
    e = ListNode(8)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    e = ListNode(1)
    f = ListNode(2)
    g = ListNode(6)
    e.next = f
    f.next = g
    solution = Solution()
    head = solution.mergeTwoLists(a,e)
    node = head
    while node is not None:
        print node.val
        node = node.next
    pass
            
if __name__ == '__main__': 
    main()