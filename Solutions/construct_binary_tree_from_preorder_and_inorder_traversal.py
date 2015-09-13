#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Construct Binary Tree from Preorder and Inorder Traversal] in LeetCode.

Created on: Nov 19, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    # @ICY: dfs, first element of preorder is the root , 
    #       left and right subtree is devided from inorder list
    def buildTree(self, preorder, inorder):
        length = len(preorder)
        if length:
            rootval = preorder[0]
            for i in range(length):
                if inorder[i] == rootval:
                    index = i
                    break
            root = TreeNode(rootval)
            root.left = self.buildTree(preorder[1:index+1], inorder[:index]) 
            root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
            return root
        else:
            return None

#----------------------------SELF TEST----------------------------#

def main():
    inorder = [2,1,3]
    preorder = [1,2,3]
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    print root.val
    print root.left.val
    print root.right.val
    pass
            
if __name__ == '__main__': 
    main()