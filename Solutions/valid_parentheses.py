#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Valid Parentheses] in LeetCode.

Created on: Nov 6, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {
                '(':')',
                ')':'(',
                '[':']',
                ']':'[',
                '{':'}',
                '}':'{',
                }

        for item in s:
            if stack == [] or dict[item] != stack[len(stack)-1]:
                stack.append(item)
            elif dict[item] == stack[len(stack)-1]:
                stack.pop()
        return stack == []
        

#----------------------------SELF TEST----------------------------#

def main():
    test_string = '()[]{}'
    test_string = '([)]'
    solution = Solution()
    print solution.isValid(test_string)
            
if __name__ == '__main__': 
    main()