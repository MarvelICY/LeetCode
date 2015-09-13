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
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    # @ICY: hash table, dfs, hard, reprint
    def findLadders(self, start, end, dict):

        dict.add(end)
        q = []
        q.append((start, 1))
        while q:
            curr = q.pop(0)
            curr_word = curr[0]
            curr_len = curr[1]
            if curr_word == end: return curr_len
            for i in range(len(start)):
                part1 = curr_word[:i]   #constant optimize
                part2 = curr_word[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if curr_word[i] != j:
                        nextword = part1 + j + part2
                        if nextword in dict:
                            q.append((nextword, curr_len+1))
                            dict.remove(nextword)
        return 0

#----------------------------SELF TEST----------------------------#

def main():
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]
    dict = set(dict)
    solution = Solution()
    print solution.findLadders(start, end, dict)
    pass
            
if __name__ == '__main__': 
    main()