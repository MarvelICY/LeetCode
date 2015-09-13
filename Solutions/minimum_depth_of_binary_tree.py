#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Minimum Depth of Binary Tree] in LeetCode.

Created on: Nov 13, 2014

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
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        self.depth = 99999
        self.leaf_depth(root,1)
        return self.depth

    def leaf_depth(self,root,temp_depth):
        if root.left == None and root.right == None:
            if temp_depth < self.depth:
                self.depth = temp_depth
        if root.left:
            self.leaf_depth(root.left, temp_depth+1)
        if root.right:
            self.leaf_depth(root.right, temp_depth+1)

#----------------------------SELF TEST----------------------------#

def main():
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)
    root.left = a
    root.right = b
    a.left = c
    c.left = e
    a.right = d
    solution = Solution()
    print solution.minDepth(root)
    pass
            
if __name__ == '__main__': 
    main()