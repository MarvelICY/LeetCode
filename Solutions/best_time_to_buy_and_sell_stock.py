#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Best Time to Buy and Sell Stock] in LeetCode.

Created on: Nov 12, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param prices, a list of integer
    # @return an integer
    # dynamic programming
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1:
            return 0
        profit = 0

        p_prev = [0 for i in range(length)]
        p_post = [0 for i in range(length)]
        p_prev[0] = 0
        lowest = prices[0]
        for index in range(1,length):
            lowest = min(lowest, prices[index])
            p_prev[index] = max(p_prev[index-1], prices[index]-lowest)

        #careful record the highest price
        p_post[length-1] = 0
        highest = prices[length-1]
        for index in range(length-2,-1,-1):
            highest = max(highest, prices[index])
            p_post[index] = max(p_post[index+1], highest-prices[index])

        for i in range(length):
            if profit < p_prev[i] + p_post[i]:
                profit = p_prev[i] + p_post[i]
        return profit

#----------------------------SELF TEST----------------------------#

def main():
    p = [1,2,4,56,2,3,45,4,3,2]
    p = [1,2,3,1,2,3]
    p = [1,2,4]
    solution = Solution()
    print solution.maxProfit(p)
    pass
            
if __name__ == '__main__': 
    main()