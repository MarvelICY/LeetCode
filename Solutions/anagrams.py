#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Anagrams] in LeetCode.

Created on: Nov 12, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dict = {}
        result = []
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in dict:
                dict[sorted_string].append(string)
            else:
                dict[sorted_string] = [string]
        for item in dict:
            if len(dict[item]) >= 2:
                result += dict[item]    #return all groups!
        return result

        

#----------------------------SELF TEST----------------------------#

def main():
    strs = ["tea","and","ate","eat","dan"]
    solution = Solution()
    print solution.anagrams(strs)
    pass
            
if __name__ == '__main__': 
    main()