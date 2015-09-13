#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Zigzag Conversion] in LeetCode.

Created on: Nov 6, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a string
    # when row is 4, the string is like this:
    # 1   7     13
    # 2 6 8  12 14 
    # 3 5 9  11 15
    # 4   10    16
    def convert(self, s, nRows):
        if nRows <= 1:
            return s
        temp = ['' for i in range(nRows)]   #lists of string to record every line
        index = -1      #row indicator
        step = 1    #set the moving direction and step
        for i in range(len(s)):
            index = index + step
            if index == nRows:
                index = index - 2;
                step = -1
            elif index == -1:
                index = 1 
                step = 1
            print index
            temp[index] = temp[index] + s[i]
        return ''.join(temp)
        
        

#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'leedcode'
    nRows = 4
    solution = Solution()
    print solution.convert(test_string,nRows)
    pass
            
if __name__ == '__main__': 
    main()