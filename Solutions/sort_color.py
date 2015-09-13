#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Sort Colors] in LeetCode.

Created on: Nov 10, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        r_index = 0
        b_index = len(A)-1
        i = 0
        while i <= b_index:      #careful
            if A[i] == 0:
                A[r_index],A[i] = A[i],A[r_index]
                r_index += 1
                i += 1
            elif A[i] == 2:
                A[b_index],A[i] = A[i],A[b_index]
                b_index -= 1
            else:
                i += 1


#----------------------------SELF TEST----------------------------#

def main():
    test_list = [1,0,2,1,2,0,1,1,2,0,1,2]
    #test_list = [1,0,0,2,0,1]
    test_list = [1,0]
    solution = Solution()
    solution.sortColors(test_list)
    print test_list
    pass
            
if __name__ == '__main__': 
    main()