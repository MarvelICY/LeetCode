#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Edit Distance] in LeetCode.

Created on: Nov 20, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return an integer
    # @ICY: dp
    def minDistance(self, word1, word2):
        row_max = len(word1) + 1
        col_max = len(word2) + 1
        dp = [[0 for i in range(col_max)] for j in range(row_max)]
        for row in range(row_max):
            dp[row][0] = row
        for col in range(col_max):
            dp[0][col] = col
        #print dp
        for row in range(1,row_max):
            for col in range(1,col_max):
                dp[row][col] = min(min(dp[row-1][col]+1, dp[row][col-1]+1),
                                    dp[row-1][col-1] + (0 if word1[row-1] == word2[col-1] else 1))

        return dp[row_max-1][col_max-1] 
        

#----------------------------SELF TEST----------------------------#

def main():
    word1 = 'abcd'
    word2 = 'cba'
    solution = Solution()
    print solution.minDistance(word1,word2)
    pass
            
if __name__ == '__main__': 
    main()