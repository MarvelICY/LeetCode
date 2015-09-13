#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Add Binary] in LeetCode.

Created on: Nov 10, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]
        index = 0
        flag = 0    #carry
        sum = '' 
        while index < len(a) and index < len(b):
            tmp_sum = int(a[index]) + int(b[index]) + flag 
            digit = tmp_sum % 2
            sum += str(digit)
            flag = tmp_sum / 2
            index += 1

        while index <len(a):
            tmp_sum = int(a[index]) + flag 
            digit = tmp_sum % 2
            sum += str(digit)
            flag = tmp_sum / 2
            index += 1

        while index <len(b):
            tmp_sum = int(b[index]) + flag 
            digit = tmp_sum % 2
            sum += str(digit)
            flag = tmp_sum / 2
            index += 1

        if flag == 1:
            sum += '1'
        return sum[::-1]

#----------------------------SELF TEST----------------------------#

def main():
    a = '11'
    b = '1'
    solution = Solution()
    print solution.addBinary(a,b)
    pass
            
if __name__ == '__main__': 
    main()