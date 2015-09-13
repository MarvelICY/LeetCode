#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Path Sum] in LeetCode.

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

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()