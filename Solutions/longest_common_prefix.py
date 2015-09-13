#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Longest Common Prefix ] in LeetCode.

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        prefix = ''
        min_length = 99999999
        for i in range(len(strs)):
            if len(strs[i]) < min_length:
                min_length = len(strs[i])
                index = i
        shortest_str = strs[index]
        
        flag = True
        length = 0
        for i in range(min_length):
            for str in strs:
                if shortest_str[i] != str[i]:
                    flag = False
                    break
            if not flag:
                break
            length += 1
        
        return shortest_str[:length]
        
        

#----------------------------SELF TEST----------------------------#

def main():
    strs = ['abcde',
            'abcd',
            'abc',
            'abcedr']
    solution = Solution()
    print solution.longestCommonPrefix(strs)
    pass
            
if __name__ == '__main__': 
    main()