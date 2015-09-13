#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Multiply Strings] in LeetCode.

Created on: Nov 27, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    # @ICY: big number multiply
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        tmp = [0 for i in range(len(num1)+len(num2))]
        result = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp[i+j] += int(num1[i]) * int(num2[j])

        for i in range(len(tmp)):
            digit = tmp[i] % 10
            carry = tmp[i] / 10
            if i < len(tmp) - 1:
                tmp[i+1] += carry
            result.append(str(digit))

        result = result[::-1]
        while result[0] == '0' and len(result) > 1:
            del result[0]
        result = ''.join(result)
        return result

        
#----------------------------SELF TEST----------------------------#

def main():
    num1 = '188'
    num2 = '24'
    solution = Solution()
    print solution.multiply(num1,num2)
    pass
            
if __name__ == '__main__': 
    main()