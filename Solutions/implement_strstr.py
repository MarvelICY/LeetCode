#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Implement strStr()] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    # sunday

    def strStr(self, haystack, needle):
        h_length = len(haystack)
        n_length = len(needle)
        if h_length == 0 and n_length == 0 or n_length == 0:
            return 0  
        i = 0
        j = 0
        while i + j < h_length and j < n_length:
            if haystack[i+j] == needle[j]:
                if j == n_length - 1:
                    return i
                else:
                    j += 1
                continue
            else:
                j = 0
                if i + n_length >= h_length:
                    return -1
                temp_index = self.get_index(needle, n_length, haystack[i+n_length])
                if temp_index == -1:
                    i += n_length
                else:
                    i += n_length - temp_index
            if i + n_length > h_length:
                return -1
        return -1

    def get_index(self,needle,length,letter):
        for i in range(length-1,-1,-1):
            if needle[i] == letter:
                return i
        return -1



#----------------------------SELF TEST----------------------------#

def main():
    haystack = 'abcdedge'
    needle = 'ded'
    haystack = '123'
    needle = ''
    solution = Solution()
    print solution.strStr(haystack,needle)
    pass
            
if __name__ == '__main__': 
    main()