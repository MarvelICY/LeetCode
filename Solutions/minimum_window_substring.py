#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Minimum Window Substring] in LeetCode.

Created on: Nov 28, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a string
    # @ICY: hast table * 2, duplication allowed
    # @reprint
    def minWindow(self, S, T):
        

#----------------------------SELF TEST----------------------------#

def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    print solution.minWindow(s, t)
    pass
            
if __name__ == '__main__': 
    main()