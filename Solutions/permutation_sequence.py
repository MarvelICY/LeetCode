#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Regular Expression Matching] in LeetCode.

Created on: Nov 24, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a string
    # @ICY: recurse
    def getPermutation(self, n, k):
        self.nums = []
        self.result = ''
        for i in range(n):
            self.nums.append(i+1)
        self.permutation(self.nums, n, k)
        return self.result

    def permutation(self, nums, n, k):

        if len(nums) == 1:
            self.result += str(nums[0])
            return

        m = 0 
        fac = 1
        for i in range(2,n):
            fac = fac * i 
        
        while k > (m + 1) * fac:
            m += 1
        self.result += str(nums[m])

        self.permutation(nums[:m]+nums[m+1:], n-1, k-m*fac)  
        

#----------------------------SELF TEST----------------------------#

def main():
    n = 1
    k = 1
    solution = Solution()
    print solution.getPermutation(n, k)
    pass
            
if __name__ == '__main__': 
    main()