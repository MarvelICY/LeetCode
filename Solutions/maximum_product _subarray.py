#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: Solution of [Maximum Product Subarray] in LeetCode.

Created on: Oct 24, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a list of lists of integers
    # Dynamic Programming: O(n)
    def maxProduct(self, A):
        product = A[0]
        maxProduct = A[0]
        minProduct = A[0]
        for i in range(1,len(A)):
            temp_max = maxProduct
            temp_min = minProduct
            maxProduct = self.Get_Max(A[i], A[i]*temp_max, A[i]*temp_min)     #keep the max and min as production is sensitive to the sign
            minProduct = self.Get_Min(A[i], A[i]*temp_max, A[i]*temp_min)
            if maxProduct > product:
                product = maxProduct
        return product

    def Get_Max(self,a,b,c):
        output = a if a > b else b
        output = c if c > output else output
        return output

    def Get_Min(self,a,b,c):
        output = a if a < b else b
        output = c if c < output else output
        return output

#----------------------------SELF TEST----------------------------#

def main():
    #test_array = [1,2,3,0,-1,6,8,-5,3,2]
    test_array = [2,3,-4,6,5]
    test_array = [-2,-3,-4]
    solution = Solution()
    print solution.maxProduct(test_array)
    pass
            
if __name__ == '__main__': 
    main()