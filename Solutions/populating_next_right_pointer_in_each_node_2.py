#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Populating Next Right Pointers in Each Node II] in LeetCode.

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
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.left:
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.left.next = tmp.left
                        break
                    if tmp.right:
                        root.left.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.right:
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            self.connect(root.right)    #careful, right first
            self.connect(root.left)


#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()