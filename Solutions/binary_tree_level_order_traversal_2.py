#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Binary Tree Level Order Traversal II] in LeetCode.

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
    # @return a list of lists of integers
    # dsf
    def levelOrder(self, root):
        if root == None:
            return []
        self.result = []
        self.traversal(root,0)
        return self.result[::-1]

    def traversal(self,root,level):
        if root:
            if level >= len(self.result):
                self.result.append([])
            self.result[level].append(root.val)
            self.traversal(root.left, level+1)
            self.traversal(root.right, level+1)


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
    print solution.levelOrder(root)
    pass
            
if __name__ == '__main__': 
    main()