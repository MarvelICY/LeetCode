#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Insertion Sort List] in LeetCode.

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
# @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)                         
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:      #insertion element is curr.next      
                pre = dummy                         
                while pre.next.val < curr.next.val: #skip the value smaller than curr.next
                    pre = pre.next
                tmp = curr.next                     
                curr.next = tmp.next    #insert the element
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next
        

#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()