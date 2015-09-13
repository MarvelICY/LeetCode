#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Convert Sorted List to Binary Search Tree] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        list = []
        curr = head
        while curr:
            list.append(curr.val)
            curr = curr.next
        root = self.sorted_array_to_bst(list)
        return root

    def sorted_array_to_bst(self,list):
        length = len(list)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(list[0])
        root = TreeNode(list[length/2])
        root.left = self.sorted_array_to_bst(list[:length/2])
        root.right = self.sorted_array_to_bst(list[length/2+1:])
        return root

#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()