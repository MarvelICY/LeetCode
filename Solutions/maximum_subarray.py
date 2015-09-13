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
    # @param A, a list of integers
    # @return an integer
    # dp, O(n)
    def maxSubArray(self, A):
        if A == []:
            return 0
        sum = A[0]
        temp = 0
        for i in range(len(A)):
            if temp < 0:
                temp = 0        #temp record the nearest subarray with sum>=0
            temp = temp + A[i]
            sum = max(sum,temp)
        return sum

        

        

#----------------------------SELF TEST----------------------------#

def main():
    list = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print solution.maxSubArray(list)
    pass
            
if __name__ == '__main__': 
    main()