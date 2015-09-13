#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Binary Tree Maximum Path Sum] in LeetCode.

Created on: Nov 18, 2014

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
    # @ICY: dfs, there will be node value < 0, careful
    def maxPathSum(self, root):     #compare 3 situations
        self.result = -99999999
        if root == None:
            return 0
        self.sub_max(root)
        return self.result

    def sub_max(self, root):
        if root == None:
            return 0
        sum = root.val
        lmax = 0
        rmax = 0
        if root.left:
            lmax = self.sub_max(root.left)
            if lmax > 0:
                sum += lmax
        if root.right:
            rmax = self.sub_max(root.right)
            if rmax > 0:
                sum += rmax
        self.result = max(self.result, sum)
        return max(root.val, max(root.val+lmax, root.val+rmax))

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
    print solution.maxPathSum(root)
    pass
            
if __name__ == '__main__': 
    main()