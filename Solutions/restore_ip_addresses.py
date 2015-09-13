#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Restore IP Addresses] in LeetCode.

Created on: Nov 27, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.result = []
        self.dfs(0, s, '')
        return self.result

    def dfs(self, index, s, tmp_result):
        if index == 4:
            if s == '' and (tmp_result[:-1] not in self.result):
                self.result.append(tmp_result[:-1])
            return 
        length = min(3, len(s))     #careful
        for i in range(length):
            num = int(s[:i+1])
            if num == 0:        #careful
                self.dfs(index+1, s[i+1:], tmp_result+str(num)+'.')
                break
            if num > 0 and num <= 255:
                self.dfs(index+1, s[i+1:], tmp_result+str(num)+'.')

        
#----------------------------SELF TEST----------------------------#

def main():
    test_string = '25525511135'
    test_string = '010010'
    solution = Solution()
    print solution.restoreIpAddresses(test_string)
    pass
            
if __name__ == '__main__': 
    main()