#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Combination Sum] in LeetCode.

Created on: Nov 19, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    # @ICY: dfs
    def combinationSum(self, candidates, target):
        self.result = []
        candidates.sort()
        self.candidates = candidates
        self.length = len(self.candidates)
        self.dfs(0, target, [])
        return self.result

    def dfs(self, index, target, tmp_result):
        if target == 0:
            self.result.append(tmp_result)
            return
        for i in range(index, self.length):
            if target < self.candidates[i]:
                return
            self.dfs(i, 
                     target-self.candidates[i], 
                     tmp_result+[self.candidates[i]])

#----------------------------SELF TEST----------------------------#

def main():
    list = [2,3,6,7]
    target = 7
    solution = Solution()
    print solution.combinationSum(list, target)
    pass
            
if __name__ == '__main__': 
    main()