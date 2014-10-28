#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Minimum in Rotated Sorted Array II] in LeetCode.

Created on: Oct 24, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param num, a list of integer
    # @return an integer
    #Traversal:O(n)
    def findMin(self, num):
        value=num[0]
        for index in range(0,len(num)):
            if value > num[index]:
                value=num[index]
        return value


#----------------------------SELF TEST----------------------------#

def main():
    test_array=[2,3,4,0,1]
    #test_array=[4,5,6,7,0,1,2]
    #test_array=[0,1]
    #test_array=[1,0]
    #test_array=[11,1,1,2,3,3,4]
    test_array=[0,0,-2,0]
    #test_array=[1,3,3]
    solution=Solution()
    print solution.findMin(test_array)
    pass
            
if __name__ == '__main__': 
    main()
    
    
    