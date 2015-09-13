#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Regular Expression Matching] in LeetCode.

Created on: Nov 28, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a boolean
    # @ICY: dp,reprint
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]

#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'leedcode'
    test_pattern = 'le*'
    solution = Solution()
    print solution.isMatch(test_string,test_pattern)
    pass
            
if __name__ == '__main__': 
    main()