#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Longest Valid Parentheses] in LeetCode.

Created on: Nov 27, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param s, a string
    # @return an integer
    # @ICY: reprint,stack,O(n)
    def longestValidParentheses(self, s):
        result = 0
        start_index = -1
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack == []:
                start_index = i     #denote the beginning position
            else:
                stack.pop()
                if stack == []:
                    result = max(result, i - start_index)
                else:
                    result = max(result, i - stack[len(stack)-1])
        return result


#----------------------------SELF TEST----------------------------#

def main():
    test_string = '()()))())()))('
    test_string = ')()'
    solution = Solution()
    print solution.longestValidParentheses(test_string)
    pass
            
if __name__ == '__main__': 
    main()