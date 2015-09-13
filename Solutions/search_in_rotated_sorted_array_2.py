#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Search in Rotated Sorted Array II] in LeetCode.

Created on: Nov 17, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    # @ICY: binary search
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            middle = (left + right) / 2
            if A[middle] == target:
                return True
            if A[left] == A[middle] == A[right]:
                left = left + 1
                right = right - 1
            elif A[middle] >= A[left]:
                if target >= A[left] and target < A[middle]:     #boundary =
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target > A[middle] and target <= A[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return False
        

#----------------------------SELF TEST----------------------------#

def main():
    test_array = [7,8,9,9,2,3,4,5,5]
    test_array = [3,1,1]
    target = 0
    solution = Solution()
    print solution.search(test_array,target)
    pass
            
if __name__ == '__main__': 
    main()