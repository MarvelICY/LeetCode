#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Validate Binary Search Tree] in LeetCode.

Created on: Nov 12, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    def isValidBST(self, root):
        return self.ValidBST(root, -2147483648, 2147483647)

    def ValidBST(self, root, min, max):     #update the value of min and max recursively
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)
    
#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()