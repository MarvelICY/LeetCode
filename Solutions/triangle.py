#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Triangle] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    # dp
    def minimumTotal(self, triangle):
        if triangle == [] or triangle == [[]]:
            return 0
        dp = [0 for i in range(len(triangle))]
        temp = [0 for i in range(len(triangle))]
        dp[0] = triangle[0][0]
        for i in range(1,len(triangle)):
            temp[0] = dp[0] + triangle[i][0]
            temp[len(triangle[i])-1] = dp[len(triangle[i])-2] + triangle[i][len(triangle[i])-1]
            for j in range(1,i):
                temp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp = temp[:]    #careful, deep copy
        dp.sort()
        return dp[0]
        

#----------------------------SELF TEST----------------------------#

def main():
    triangle = [     [2],
                    [3,4],
                   [6,5,7],
                  [4,1,8,3]
                ]
    triangle = [[12]]
    solution = Solution()
    print solution.minimumTotal(triangle)
    pass
            
if __name__ == '__main__': 
    main()