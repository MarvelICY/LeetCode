#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Pascal's Triangle II] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        temp = [1,1]
        result = []
        for i in range(3,rowIndex+2):
            result = [1 for k in range(i)]
            for j in range(1,i-1):
                result[j] = temp[j-1] + temp[j]
            temp = result
        return result
        

#----------------------------SELF TEST----------------------------#

def main():
    index = 4
    solution = Solution()
    print solution.getRow(index)
    pass
            
if __name__ == '__main__': 
    main()