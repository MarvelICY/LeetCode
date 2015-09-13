#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Regular Expression Matching] in LeetCode.

Created on: Nov 18, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param s, a string
    # @return a list of lists of string
    # @ICY: dfs
    def partition(self, s):
        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s , tmp_result):
        if len(s) == 0:
            self.result.append(tmp_result)
        for i in range(0, len(s)):
            if self.is_palindrome(s[:i+1]):
                self.dfs(s[i+1:], tmp_result+[s[:i+1]])
                
    def is_palindrome(self, s):
        for i in range(0,len(s)/2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
        

#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'aabacab'
    solution = Solution()
    print solution.partition(test_string)
    pass
            
if __name__ == '__main__': 
    main()