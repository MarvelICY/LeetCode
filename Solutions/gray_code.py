#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Gray Code] in LeetCode.

Created on: Nov 17, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        result = []
        size = 1 << n    #Bit manipulation
        for i in range(size):
            result.append((i>>1)^i)
        return result

        
#----------------------------SELF TEST----------------------------#

def main():
    n = 0
    solution = Solution()
    print solution.grayCode(n)
    pass
            
if __name__ == '__main__': 
    main()