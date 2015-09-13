#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Longest Consecutive Sequence] in LeetCode.

Created on: Nov 17, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {}
        result = -1 
        for i in num:
            if i not in dict:
                dict[i] = False

        for i in dict:      # mark every digit only once 
            if dict[i] == False:
                curr = i+1
                lenright = 0
                while curr in dict:     # -->
                    lenright += 1
                    dict[curr] = True
                    curr += 1
                curr = i-1
                lenleft = 0
                while curr in dict:     # <--
                    lenleft += 1
                    dict[curr] = True
                    curr -= 1
                result = max(result, lenleft+1+lenright)
        return result

#----------------------------SELF TEST----------------------------#

def main():
    array = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    print solution.longestConsecutive(array)
    pass
            
if __name__ == '__main__': 
    main()