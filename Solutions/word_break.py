#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Word break] in LeetCode.

Created on: Nov 6, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dp = [False for i in range(len(s)+1)] # dp[i+1] denote the substring with length i
        dp[0] = True
        for i in range(1,len(s)+1):
            for k in range(i):      #check the additional word [k:i]
                if dp[k] and s[k:i] in dict: 
                    dp[i] = True
        return dp[len(s)]
        
        

#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'leetcode'
    test_dict = ['leet','code']
    solution = Solution()
    print solution.wordBreak(test_string,test_dict)
    pass
            
if __name__ == '__main__': 
    main()