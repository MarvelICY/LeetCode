#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Word Break II] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.result = []
        self.dfs(s, dict, '')
        return self.result

    def dfs(self,s,dict,out_string):
        if self.check(s,dict):
            if len(s) == 0:
                self.result.append(out_string[1:])
            for i in range(1,len(s)+1):     #careful
                if s[:i] in dict:       #s[:i]== s(0~i-1)
                    self.dfs(s[i:], dict, out_string+' '+s[:i])    #the fisrt char will always be ' '

    def check(self,s,dict):   
        #check the appropirate substring
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1,len(s)+1):     #careful
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]



        

#----------------------------SELF TEST----------------------------#

def main():
    s = 'catsanddog'
    dict = ["cat", "cats", "and", "sand", "dog"]
    solution = Solution()
    print solution.wordBreak(s,dict)
    print s[:1]
    pass
            
if __name__ == '__main__': 
    main()