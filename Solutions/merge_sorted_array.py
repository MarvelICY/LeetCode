#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Merge Sorted Array] in LeetCode.

Created on: Nov 12, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        index_a = 0
        index_b = 0
        while index_a < len(A) and index_b < len(B):
            if A[index_a] > B[index_b]:
                A.insert(index_a, B[index_b])
                index_a += 1
                index_b += 1
            else:
                index_a += 1
        while index_b < len(B):
            A.append(B[index_b])
            index_b += 1
        
        
#----------------------------SELF TEST----------------------------#

def main():
    A = [1,2,3,5,6,7,8,9,10]
    B = [4,6,8]
    A = []
    B = [1]
    solution = Solution()
    print solution.merge(A,9,B,3)
    print len(A)
    pass
            
if __name__ == '__main__': 
    main()