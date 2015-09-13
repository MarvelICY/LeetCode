#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Sum Root to Leaf Numbers] in LeetCode.

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
    # @return an integer
    def sumNumbers(self, root):
        return add_path(root, 0)

    def add_path(self, root, path_sum):
        if root == None:
            return 0
        path_sum = path_sum * 10 + root.val
        if root.left == None and root.right == None:
            return path_sum
        return self.add_path(root.left, path_sum) + self.add_path(root.right, path_sum)



        
    
#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()