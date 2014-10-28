#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Solution of [Pascal Triangle I] in LeetCode.

Created on: Oct 15, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        list = []          
        if numRows == 0:
            return list  
        list.append([1])
        for i in range(2,numRows+1):  #calculate every row of the triangle
            templist = [1]
            for j in range(1,i-1):
                templist.append(list[i-2][j-1] + list[i-2][j])
            templist.append(1)
            list.append(templist)
        return list

#----------------------------SELF TEST----------------------------#

def main():
    solution = Solution()
    print solution.generate(0)
    print solution.generate(3)
    print solution.generate(5)
    pass
            
if __name__ == '__main__': 
    main()
    
    
    