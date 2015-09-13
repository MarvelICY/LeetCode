#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Largest Rectangle in Histogram] in LeetCode.

Created on: Nov 24, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param height, a list of integer
    # @return an integer
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
    test_list = [2,1,5,6,2,3]
    test_list = [2,1,2]
    solution = Solution()
    print solution.largestRectangleArea(test_list)
    pass
            
if __name__ == '__main__': 
    main()