#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Combinations] in LeetCode.

Created on: Nov 17, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a list of lists of integers
    # @ICY: dfs
    def combine(self, n, k):
        self.k = k
        self.n = n
        self.count = 0      #record the length of the combination
        self.result = []
        self.dfs(1, [])
        return self.result

    def dfs(self, start, tmp_result):
        if self.count == self.k:
            self.result.append(tmp_result)
            return 
        for i in range(start,self.n+1):
            self.count += 1
            self.dfs(i+1,tmp_result+[i])
            self.count -= 1                 
        
        
        

#----------------------------SELF TEST----------------------------#

def main():
    n = 5
    k = 2
    solution = Solution()
    print solution.combine(n,k)
    pass
            
if __name__ == '__main__': 
    main()