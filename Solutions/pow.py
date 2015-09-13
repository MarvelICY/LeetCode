#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Pow(x,n)] in LeetCode.

Created on: Nov 10, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1.0 / self.pow(x,-n)
        elif n % 2:
            return self.pow(x*x,n/2) * x
        else:
            return self.pow(x*x,n/2)

        
#----------------------------SELF TEST----------------------------#

def main():
    val = 5
    n = -10
    solution = Solution()
    print solution.pow(val,n)
    pass
            
if __name__ == '__main__': 
    main()