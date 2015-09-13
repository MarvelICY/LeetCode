#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Length of Last Word] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        #remove space in the tail of the string
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                s = s[:i+1]
                break
        list = s.split(' ')
        print list
        return len(list[len(list)-1])


        
        
        

#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'leed code'
    test_string = 'le asd wefsda'
    test_string = 'a '
    solution = Solution()
    print solution.lengthOfLastWord(test_string)
    pass
            
if __name__ == '__main__': 
    main()