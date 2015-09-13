#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Regular Expression Matching] in LeetCode.

Created on: Nov 19, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    # @ICY: binary search
    def searchRange(self, A, target):
        left = 0
        right = len(A) - 1

        while left <= right:
            middle = (left + right) / 2
            if A[middle] == target:
                break
            elif A[middle] > target:
                right = middle - 1
            elif A[middle] < target:
                left = middle + 1
        
        if left > right:
            return [-1,-1]

        left = middle
        right = middle
        while left > 0:

            if A[left-1] != target:
                break
            left -= 1
        while right < len(A)-1:
            if A[right+1] != target:
                break
            right += 1

        return [left,right]
        

#----------------------------SELF TEST----------------------------#

def main():
    list = [7, 7, 7, 8, 8, 8]
    target = 8
    solution = Solution()
    print solution.searchRange(list, target)
    pass
            
if __name__ == '__main__': 
    main()