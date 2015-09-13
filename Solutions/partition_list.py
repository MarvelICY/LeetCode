#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Partition List] in LeetCode.

Created on: Nov 13, 2014

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
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummy_1 = ListNode(0)
        dummy_2 = ListNode(0)
        temp = head
        curr_1 = dummy_1
        curr_2 = dummy_2
        while temp:
            if temp.val < x:
                curr_1.next = temp
                temp = temp.next
                curr_1 = curr_1.next
                curr_1.next = None
            elif temp.val >= x:
                curr_2.next = temp
                temp = temp.next
                curr_2 = curr_2.next
                curr_2.next = None

        curr_1.next = dummy_2.next
        return dummy_1.next


#----------------------------SELF TEST----------------------------#

def main():
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    x = 4
    solution = Solution()
    head = solution.partition(a,x)
    node = head
    while node is not None:
        print node.val
        node = node.next
            
if __name__ == '__main__': 
    main()