#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Climbing Stairs] in LeetCode.

Created on: Nov 10, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param n, an integer
    # @return an integer
    # dp
    def climbStairs(self, n):
        dp = [1 for i in range(n+1)]
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        

        
        
        

#----------------------------SELF TEST----------------------------#

def main():
    n = 10
    solution = Solution()
    print solution.climbStairs(n)
    pass
            
if __name__ == '__main__': 
    main()