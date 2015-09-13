#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Spiral Matrix II] in LeetCode.

Created on: Nov 18, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []

        result = [[0 for i in range(n)] for j in range(n)]
        num = 1

        #four boundaries
        up = 0
        bottom = len(result) - 1
        left = 0
        right = len(result[0]) - 1

        # right:0, down:1, left:2, up:3
        direct = 0
        
        while up <= bottom and left <= right:
            if direct == 0:
                for i in range(left, right+1):
                    result[up][i] = num
                    num += 1
                up += 1
            if direct == 1:
                for i in range(up, bottom+1):
                    result[i][right] = num
                    num += 1
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    result[bottom][i] = num
                    num += 1
                bottom -= 1
            if direct == 3:
                for i in range(bottom, up-1, -1):
                    result[i][left] = num
                    num += 1
                left += 1
            direct = (direct + 1) % 4   #loop 

        return result

#----------------------------SELF TEST----------------------------#

def main():
    n = 3
    solution = Solution()
    print solution.generateMatrix(n)
    pass
            
if __name__ == '__main__': 
    main()