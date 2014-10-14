# -*- coding:UTF-8 -*-
'''
Created on 2014年10月14日

@author: ICY
'''

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        list=[]          
        if numRows == 0:
            return list  
        list.append([1])
        for i in range(2,numRows+1):
            templist=[1]
            for j in range(1,i-1):
                templist.append(list[i-2][j-1]+list[i-2][j])
            templist.append(1)
            list.append(templist)
        return list

#----------------------------self test--------------------------------#            
if __name__ == '__main__':

    solution= Solution()
    print solution.generate(10)
    
    


            
            