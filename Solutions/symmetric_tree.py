#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Symmetric Tree] in LeetCode.

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
    # @return a boolean
    # recurse
    def isSymmetric(self, root):
        if root:
            return self.symm_traversal(root.left, root.right)
        return True

    def symm_traversal(self,p,q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.symm_traversal(p.left, q.right) \
                    and self.symm_traversal(p.right,q.left)
        return False
        

#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'leedcode'
    test_dict = ['leet','code']
    solution = Solution()
    print solution.wordBreak(test_string,test_dict)
    pass
            
if __name__ == '__main__': 
    main()