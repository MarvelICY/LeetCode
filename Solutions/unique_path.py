#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Unique Paths II] in LeetCode.

Created on: Nov 18, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid == [] or obstacleGrid[0][0] == 1:
            return 0
        dp = obstacleGrid[:]
        dp[0][0] = 1

        row_max = len(obstacleGrid)
        col_max = len(obstacleGrid[0])
        for i in range(1, row_max):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

        for i in range(1, col_max):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]

        for row in range(1, row_max):
            for col in range(1, col_max):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[row_max-1][col_max-1]
        

#----------------------------SELF TEST----------------------------#

def main():
    grid = [
              [0,0,0],
              [0,1,0],
              [0,0,0]
            ]
    solution = Solution()
    print solution.uniquePathsWithObstacles(grid)
    pass
            
if __name__ == '__main__': 
    main()