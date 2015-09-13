#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Srting to Integer] in LeetCode.

Created on: Nov 10, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return an integer
    # hints: space sign and overflow
    # take care when : no-digit appears, space appears, multi signs appear
    def atoi(self, str):
        if str == '':
            return 0
        
        INT_MAX = 2147483647    #2^31
        INT_MIN = -2147483648
        sum = 0
        sign = 1
        sign_num = 0   #bug of leetcode
        exist = 0

        for letter in str:
            if letter == ' ' and exist == 0:
                continue
            if letter == '-':
                if sign_num > 0:
                    return 0
                else:
                    sign = -1
                    sign_num = 1
                    exist = 1
            elif letter == '+':
                if sign_num > 0:
                    return 0
                else:
                    sign = 1
                    sign_num = 1
                    exist = 1
            elif letter in '0123456789':
                digit = int(letter)
                if sum <= INT_MAX / 10:
                    sum = sum * 10
                else:
                    if sign == 1:
                        return INT_MAX
                    else:
                        return INT_MIN

                if sum <= INT_MAX - digit:
                    sum = sum + digit
                else:
                    if sign == 1:
                        return INT_MAX
                    else:
                        return INT_MIN
                exist = 1
            else:
                return sign * sum
        return sign * sum
        
        
        

#----------------------------SELF TEST----------------------------#

def main():
    test_string = '             -65769863'
    test_string = '  -0012a42'
    solution = Solution()
    print solution.atoi(test_string)
    pass
            
if __name__ == '__main__': 
    main()