#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Unique Binary Search Trees II] in LeetCode.

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
    # @return a list of tree node
    # @ICY: dfs, reprint
    def generateTrees(self, n):
        return self.dfs(1, n)

    def dfs(self, start, end):
        result = []
        if start > end:
            return [None]   #careful
        for root_val in range(start, end+1):
            left_tree = self.dfs(start,root_val-1)
            right_tree = self.dfs(root_val+1,end)
            for i in left_tree:
                for j in right_tree:
                    root = TreeNode(root_val)
                    root.left = i
                    root.right = j
                    result.append(root)
        return result


#----------------------------SELF TEST----------------------------#

def main():
    n = 6
    solution = Solution()
    print solution.generateTrees(n)
    pass
            
if __name__ == '__main__': 
    main()