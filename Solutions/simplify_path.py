#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Simplify Path] in LeetCode.

Created on: Nov 27, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        result = []
        elements = path.split('/')
        for i in range(len(elements)):
            if elements[i] != '' and elements[i] != '.':
                if elements[i] == '..':
                    if result != []:
                        result.pop()
                else:
                    result.append('/'+elements[i])
        if result == []:
            result.append('/')
        return ''.join(result)

#----------------------------SELF TEST----------------------------#

def main():
    test_string = '/a/./b/../../c/'
    test_string = '/../'
    test_string = '///'
    solution = Solution()
    print solution.simplifyPath(test_string)
    pass
            
if __name__ == '__main__': 
    main()