#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Scramble String] in LeetCode.

Created on: Nov 24, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a boolean
    # @ICY: dfs recurse
    def isScramble(self, s1, s2):
        #compare
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        # pruning
        l1=list(s1)
        l2=list(s2)
        l1.sort()
        l2.sort()
        if l1!=l2:
            return False

        #check every division position and recurse
        length = len(s1)
        for index in range(1,length):
            if self. isScramble(s1[:index], s2[:index]) and \
                self.isScramble(s1[index:], s2[index:]):
                return True
            if self. isScramble(s1[:index], s2[length-index:]) and \
                self.isScramble(s1[index:], s2[:length-index]):
                return True

        return False

#----------------------------SELF TEST----------------------------#

def main():
    str1 = 'rgtae'
    str2 = 'great'
    str1 = 'abcdefghijklmn'
    str2 = 'efghijklmncadb'
    solution = Solution()
    print solution.isScramble(str1, str2)
    pass
            
if __name__ == '__main__': 
    main()