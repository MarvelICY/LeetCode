#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Valid Number] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param s, a string
    # @return a boolean
    # reprint
    def isNumber(self, s):
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        EXP = 5

        transfer_matrix=[[-1,  0,  3,  1,  2, -1],    #0 no input or just spaces 
                         [-1,  8, -1,  1,  4,  5],    #1 input is digits 
                         [-1, -1, -1,  4, -1, -1],    #2 no digits in front just Dot 
                         [-1, -1, -1,  1,  2, -1],    #3 sign 
                         [-1,  8, -1,  4, -1,  5],    #4 digits and dot in front 
                         [-1, -1,  6,  7, -1, -1],    #5 input 'e' or 'E' 
                         [-1, -1, -1,  7, -1, -1],    #6 after 'e' input sign 
                         [-1,  8, -1,  7, -1, -1],    #7 after 'e' input digits 
                         [-1,  8, -1, -1, -1, -1]]    #8 after valid input input space

        status = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                skip = SPACE
            elif s[i] in '-+':
                skip = SIGN
            elif s[i] in '0123456789':
                skip = DIGIT
            elif s[i] == '.':
                skip = DOT
            elif s[i] in 'eE':
                skip = EXP
            else:
                skip = INVALID

            status = transfer_matrix[status][skip]

            if status == -1:
                return False
            else:
                i += 1
        return status == 1 or status == 4 or status == 7 or status == 8

#----------------------------SELF TEST----------------------------#

def main():
    test_string = '0.1578'
    test_string = '        -75e-16    '
    solution = Solution()
    print solution.isNumber(test_string)
    pass
            
if __name__ == '__main__': 
    main()