#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Construct Binary Tree from Inorder and Postorder Traversal] in LeetCode.

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
    # @ICY: dfs, last element of postorder is the root , 
    #       left and right subtree is devided from inorder list
    def buildTree(self, inorder, postorder):
        length = len(postorder)
        if length:
            rootval = postorder[length-1]
            for i in range(length):
                if inorder[i] == rootval:
                    index = i
                    break
            root = TreeNode(rootval)
            root.left = self.buildTree(inorder[:index], postorder[:index]) 
            root.right = self.buildTree(inorder[index+1:], postorder[index:length-1])
            return root
        else:
            return None

#----------------------------SELF TEST----------------------------#

def main():
    inorder = [2,1,3]
    postorder = [2,3,1]
    solution = Solution()
    root = solution.buildTree(inorder, postorder)
    print root.val
    print root.left.val
    print root.right.val
    pass
            
if __name__ == '__main__': 
    main()