#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Interleaving String] in LeetCode.

Created on: Nov 28, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    # @ICY: hast table * 2, duplication allowed
    # @reprint
    def findSubstring(self, S, L):
        words = {}
        word_num = len(L)
        for word in L:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
        word_len = len(L[0])
        result = []
        
        #narrow down the searching range 
        for i in range(len(S)+1-word_len*word_num):     
            curr = {}
            j = 0
            while j < word_num:
                word  = S[i+j*word_len:i+(j+1)*word_len]
                if word not in words:
                    break
                if word not in curr:
                    curr[word] = 1
                else:
                    curr[word] += 1

                if curr[word] > words[word]:
                    break

                j += 1
            if j == word_num:
                result.append(i)

        return result

#----------------------------SELF TEST----------------------------#

def main():
    s = "barfoothefoobarman"
    l = ["foo", "bar"]
    solution = Solution()
    print solution.findSubstring(s, l)
    pass
            
if __name__ == '__main__': 
    main()