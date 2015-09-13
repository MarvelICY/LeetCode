#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Interleaving String] in LeetCode.

Created on: Nov 27, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a boolean
    # @ICY: TLE
    def isInterleave(self, s1, s2, s3):
        if s3 == '':
            if s1 == '' and s2 == '':
                return True 
            else:
                return False
        else:
            if s1 != '' and s2 != '':
                if s3[0] == s1[0] == s2[0]:
                    return self.isInterleave(s1[1:],s2[:],s3[1:]) or \
                            self.isInterleave(s1[:],s2[1:],s3[1:])
                elif s3[0] == s1[0]:
                    return self.isInterleave(s1[1:],s2[:],s3[1:])
                elif s3[0] == s2[0]:
                    return self.isInterleave(s1[:],s2[1:],s3[1:])
            elif s1 != '':
                return s3 == s1
            elif s2 != '':
                return s3 == s2
            return False

    # @ICY: dp
    def isInterleave2(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        
        dp[0][0] = True
        for i in range(1,len(s1)+1):
            dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]
        for i in range(1,len(s2)+1):
            dp[0][i] = dp[0][i-1] and s3[i-1] == s2[i-1]

        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or \
                            (dp[i][j-1] and s3[i+j-1] == s2[j-1])

        return dp[len(s1)][len(s2)]

#----------------------------SELF TEST----------------------------#

def main():
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbcbcac'
    #s3 = 'aadbbbaccc'
    solution = Solution()
    print solution.isInterleave2(s1, s2, s3)
    pass
            
if __name__ == '__main__': 
    main()