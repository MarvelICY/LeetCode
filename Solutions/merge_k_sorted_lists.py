#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Merge k Sorted Lists] in LeetCode.

Created on: Nov 12, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    # heap
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heap.append((node.val,node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head        
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap,(pop[1].next.val,pop[1].next))
        return head.next

#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()