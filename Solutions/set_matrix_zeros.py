#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Set Matrix Zeroes] in LeetCode.

Created on: Nov 17, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    # @ ICY: O(m+n) space
    def setZeroes(self, matrix):
        row_rd = [False for i in range(len(matrix))]
        col_rd = [False for i in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    row_rd[row] = True
                    col_rd[col] = True

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row_rd[row] == True or col_rd[col] == True:
                    matrix[row][col] = 0


        
        

#----------------------------SELF TEST----------------------------#

def main():
    matrix = [[1,2,3],
              [4,4,0],
              [0,2,3]]
    solution = Solution()
    solution.setZeroes(matrix)
    print matrix
            
if __name__ == '__main__': 
    main()