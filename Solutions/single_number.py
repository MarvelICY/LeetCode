#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Single Number] in LeetCode.

Created on: Nov 4, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for a in A:
            result = result ^ a     #xor 
        return result
        
        

#----------------------------SELF TEST----------------------------#

def main():
    test_list = [1,1,2,2,3,4,4,5,5,6,6]
    solution = Solution()
    print solution.singleNumber(test_list)
    pass
            
if __name__ == '__main__': 
    main()