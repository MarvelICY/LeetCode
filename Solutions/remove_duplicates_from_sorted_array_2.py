#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Remove Duplicates from Sorted Array II] in LeetCode.

Created on: Nov 17, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        result = 1
        for index in range(2,len(A)):
            if A[index] == A[result] and A[index] == A[result-1]:
                continue
            else:
                result += 1
                A[result] = A[index]
        return result + 1


#----------------------------SELF TEST----------------------------#

def main():
    array = [1,1,1,2,2,3,3,3,3,3,3,4,4,4,4]
    solution = Solution()
    print solution.removeDuplicates(array)
    print array

if __name__ == '__main__': 
    main()