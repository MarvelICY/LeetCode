#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Best Time to Buy and Sell Stock II] in LeetCode.

Created on: Nov 12, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param prices, a list of integer
    # @return an integer
    # greedy
    def maxProfit(self, prices):
        profit = 0
        for index in range(1,len(prices)):
            if prices[index] > prices[index-1]:
                profit += prices[index] - prices[index-1]
        return profit
        
        
        

#----------------------------SELF TEST----------------------------#

def main():
    p = [1,2,4,56,2,3,45,4,3,2]
    p = [1,2,3,1,2,3]
    solution = Solution()
    print solution.maxProfit(p)
    pass
            
if __name__ == '__main__': 
    main()