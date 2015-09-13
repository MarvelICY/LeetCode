#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Spiral Matrix] in LeetCode.

Created on: Nov 18, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        result = []
        up = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        # right:0, down:1, left:2, up:3
        direct = 0
        while up <= bottom and left <= right:
            if direct == 0:
                for i in range(left, right+1):
                    result.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, bottom+1):
                    result.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if direct == 3:
                for i in range(bottom, up-1, -1):
                    result.append(matrix[i][left])
                left += 1
            direct = (direct + 1) % 4

        return result

#----------------------------SELF TEST----------------------------#

def main():
    matrix = [
                 [ 1, 2, 3 ],
                 [ 4, 5, 6 ],
                 [ 7, 8, 9 ]
                ]
    matrix = []
    solution = Solution()
    print solution.spiralOrder(matrix)
    pass
            
if __name__ == '__main__': 
    main()