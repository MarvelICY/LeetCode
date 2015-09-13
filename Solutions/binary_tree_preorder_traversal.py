#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Binary Tree Preorder Traversal ] in LeetCode.

Created on: Nov 6, 2014

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
    # @return a list of integers
    def postorderTraversal(self, root):
        self.result = []
        self.postorder(root)
        return self.result
    
    def postorder(self,root):
        if root:
            self.result.append(root.val)
            self.postorder(root.left)
            self.postorder(root.right)


#----------------------------SELF TEST----------------------------#

def main():
    root = TreeNode(0)
    a = TreeNode(1)
    b =TreeNode(2)
    root.left = a
    root.right = b
    solution = Solution()
    print(solution.postorderTraversal(root))
    pass
            
if __name__ == '__main__': 
    main()