#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Binary Tree Zigzag Level Order Traversal] in LeetCode.

Created on: Nov 18, 2014

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
    # @return a list of lists of integers
    # @ICY: dfs
    def zigzagLevelOrder(self, root):
        self.result = []
        self.dfs(0, root)
        return self.result

    def dfs(self, level, root):
        if root:
            if len(self.result) < level + 1:
                self.result.append([])
            if level % 2 == 0:
                self.result[level].append(root.val)
            else:
                self.result[level].insert(0, root.val)
            self.dfs(level+1, root.left)
            self.dfs(level+1, root.right)
        
        
        

#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'leedcode'
    test_pattern = 'le*'
    solution = Solution()
    print solution.isMatch(test_string,test_pattern)
    pass
            
if __name__ == '__main__': 
    main()