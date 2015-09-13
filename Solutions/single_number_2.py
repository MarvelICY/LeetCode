#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Single Number II] in LeetCode.

Created on: Nov 4, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
        
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        #extra memory cost
        #O(n)
        hash_table = {}
        for a in A:
            if a in hash_table:
                hash_table[a] += 1
            else:
                hash_table[a] = 1

        for key in hash_table:
            if hash_table[key] == 1:
                return key

        

#----------------------------SELF TEST----------------------------#

def main():
    test_list = [1,1,1,2,2,2,3,4,4,4,5,5,5,6,6,6]
    solution = Solution()
    print solution.singleNumber(test_list)
    pass
            
if __name__ == '__main__': 
    main()