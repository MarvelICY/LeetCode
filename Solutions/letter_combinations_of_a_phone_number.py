#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Letter Combinations of a Phone Number] in LeetCode.

Created on: Nov 18, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.dict = {
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
        }
        self.digits = digits
        self.length = len(self.digits)
        self.result = []
        self.dfs(0, '')
        return self.result

    def dfs(self,index, tmp_string):
        if index == self.length:
            self.result.append(tmp_string)
            return
        for letter in self.dict[self.digits[index]]:
                self.dfs(index+1, tmp_string+letter)


#----------------------------SELF TEST----------------------------#

def main():
    test_string = '23'
    solution = Solution()
    print solution.letterCombinations(test_string)
    pass
            
if __name__ == '__main__': 
    main()