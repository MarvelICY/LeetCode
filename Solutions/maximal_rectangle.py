#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Maximal Rectangle] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    # @ICY: using rectanglearea algo.O(n^3)
    def maximalRectangle(self, matrix):
        if matrix == []:
            return 0
        result = 0
        row_max = len(matrix)
        col_max = len(matrix[0])
        height = [0 for i in range(col_max)]

        for row in range(row_max):
            for col in range(col_max):
                if matrix[row][col] == '1':
                    height[col] = 1 + height[col]
                else:
                    height[col] = 0
            temp_area = self.largestRectangleArea(height)
            result = max(result, temp_area)
        return result

    def largestRectangleArea(self, height):
        max_area = 0
        stack_index = []
        stack_height = []
        for i in range(len(height)):
            if stack_height == []:
                stack_height.append(height[i])
                stack_index.append(i)
            elif height[i] > stack_height[len(stack_height)-1]:
                stack_height.append(height[i])
                stack_index.append(i)
            elif height[i] < stack_height[len(stack_height)-1]:
                index = 0
                while stack_height and height[i] < stack_height[len(stack_height)-1]:
                    index = stack_index.pop()
                    temp_area = stack_height.pop() * (i - index)
                    max_area = max(max_area, temp_area)
                #add the lowest height
                stack_height.append(height[i])
                stack_index.append(index)

        while stack_height:
            temp_area = stack_height.pop() * (len(height) - stack_index.pop())
            max_area = max(max_area, temp_area)

        return max_area


#----------------------------SELF TEST----------------------------#

def main():
    matrix = ['100','011','011']
    solution = Solution()
    print solution.maximalRectangle(matrix)
    pass
            
if __name__ == '__main__': 
    main()