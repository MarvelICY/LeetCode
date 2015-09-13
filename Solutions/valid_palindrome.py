#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Valid Palindrome] in LeetCode.

Created on: Nov 6, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param s, a string
    # @return a boolean
    # O(n)
    def isPalindrome(self, s):
        s = s.lower()
        temp = [] 
        for letter in s:
            if letter in 'abcdefghijklmnopqrstuvwxyz0123456789':
                temp.append(letter)
        length = len(temp)
        for i in range(0,(length)/2):
            if temp[i] != temp[length-1-i]:
                return False
        return True

        remedy
#----------------------------SELF TEST----------------------------#

def main():
    test_string = 'A man, a plan, a canal: Panama'
    test_string = 'race a car'
    #test_string = 'aba'
    solution = Solution()
    print solution.isPalindrome(test_string)
    pass
            
if __name__ == '__main__': 
    main()