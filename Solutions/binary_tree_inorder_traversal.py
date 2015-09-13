#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Binary Tree Inorder Traversal] in LeetCode.

Created on: Nov 10, 2014

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
    # @return a list of integers
    def inorderTraversal(self, root):
        self.result = []
        self.inorder(root)
        return self.result
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.result.append(root.val)
            self.inorder(root.right)
            
        
        
#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()