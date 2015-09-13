#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Rotate Image] in LeetCode.

Created on: Nov 10, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    # exchange positions 
    def rotate(self, matrix):
        n = len(matrix)
        for row in range(n):
            for col in range(row):  #careful 
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
        for row in range(n):
            for col in range(n/2):
                matrix[row][col],matrix[row][n-1-col] = matrix[row][n-1-col],matrix[row][col]
        return matrix

#----------------------------SELF TEST----------------------------#

def main():
    matrix = [[1,2],[3,4]]
    solution = Solution()
    print solution.rotate(matrix)
    pass
            
if __name__ == '__main__': 
    main()