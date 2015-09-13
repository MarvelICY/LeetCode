#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Search Insert Position] in LeetCode.

Created on: Nov 10, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left = 0
        right = len(A) - 1
        middle = left + (right - left) // 2
        while left < right - 1:
            if target > A[middle]:
                left = middle
            elif target < A[middle]:
                right = middle
            else:
                return middle
            middle = left + (right - left) // 2
        if target <= A[left]:
            return left
        elif target > A[right]:
            return right + 1
        else:
            return right


        
#----------------------------SELF TEST----------------------------#

def main():
    test_list = [1,3,4,5,6]
    value = 7
    solution = Solution()
    print solution.searchInsert(test_list,value)
    pass
            
if __name__ == '__main__': 
    main()