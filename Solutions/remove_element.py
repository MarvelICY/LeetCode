#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Remove Element] in LeetCode.

Created on: Nov 11, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        index = 0
        while index < len(A):
            if A[index] == elem:
                A.pop(index)
            else:
                index += 1
        return len(A)
        
        

#----------------------------SELF TEST----------------------------#

def main():
    test_list = [1,2,3,4,5,62,3,4,5,6,21,4,37,8,6,3]
    value = 3
    solution = Solution()
    print solution.removeElement(test_list,value)
    pass
            
if __name__ == '__main__': 
    main()