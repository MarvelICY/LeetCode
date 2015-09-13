#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Copy List with Random Pointer] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        dummy = RandomListNode(0)

        curr = head
        while curr:
            temp = RandomListNode(curr.label)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next

        curr = head
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        old = head
        new = head.next
        newhead = head.next
        while new.next:
            old.next = new.next
            old = old.next
            new.next = old.next
            new = new.next
        old.next = None
        new.next = None        

        return newhead


#----------------------------SELF TEST----------------------------#

def main():
    a = RandomListNode(1)
    b = RandomListNode(4)
    c = RandomListNode(3)
    d = RandomListNode(2)
    e = RandomListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    a.random = e
    b.random = c
    c.random = b
    d.random = a
    e.random = d
    solution = Solution()
    head = solution.copyRandomList(a)
    node = head
    while node is not None:
        print node.label
        node = node.next
            
if __name__ == '__main__': 
    main()