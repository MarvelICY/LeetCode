#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Balanced Binary Tree] in LeetCode.

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
    def Height(self, root):
        if root == None:
            return 0
        return max(self.Height(root.left),self.Height(root.right)) + 1
    
    def isBalanced(self, root):
        if root  == None:
            return True
        if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()