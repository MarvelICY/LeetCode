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
    # @ICY: dp
    def minCut(self, s):
        length = len(s)
        cut = [i-1 for i in range(length+1)]
        
        for i in range(length):
            # odd palindrome
            j = 0
            while i - j >= 0 and i + j < length and s[i-j] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j]+1)
                j += 1
            #even palindrome
            j = 1
            while i - j + 1 >= 0 and i + j < length and s[i-j+1]==s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j+1]+1)
                j += 1
        return cut[length]
  

#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'aabacab'
    #test_string = 'abcd'
    solution = Solution()
    print solution.minCut(test_string)
    pass
            
if __name__ == '__main__': 
    main()