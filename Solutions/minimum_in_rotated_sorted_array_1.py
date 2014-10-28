#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Solution of [Minimum in Rotated Sorted Array I] in LeetCode.

Created on: Oct 24, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param num, a list of integer
    # @return an integer
    #Binary Search:O(lgn)
    def findMin(self, num):
        left = 0
        right = len(num) - 1
        value = num[left]
        while left <= right:
            middle=  left + ((right - left)>>1)   #calculate the middle index 
            if num[middle] > value:         #pivot > left and pivot > right => minimum is on the right side
                if num[middle] < num[right]:
                    return num[left]        #pivot > left and pivot < right => arrary is already sorted
                else:    
                    left = middle
                    value = num[left] #pivot <= left => minimum on the left side
            elif num[middle] < value:
                right = middle
            else:
                #compare when there are only two elements in the subarray                   
                value = num[left] if num[left] < num[right] else num[right]
                return value


#----------------------------SELF TEST----------------------------#

def main():
    test_array = [2,3,4,0,1]
    #test_array = [4,5,6,7,0,1,2]
    #test_array = [0,1]
    #test_array = [1,0]
    test_array = [1,2,3,4]
    solution = Solution()
    print solution.findMin(test_array)
    pass
            
if __name__ == '__main__': 
    main()
    
    
    