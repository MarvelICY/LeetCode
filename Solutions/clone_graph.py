#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Clone Graph] in LeetCode.

Created on: Nov 24, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @ICY: dfs
    def cloneGraph(self, node):
        if node == None:
            return None
        self.dfs(node, {})

    def dfs(self, input, map):
        if input in map:
            return map[input]
        output = UndirectedGraphNode(input.label)
        map[input] = output

        for neighbor in input.neighbors:
            output.neighbors.append(dfs(neighbor, map))
        return output
        
        
        

#----------------------------SELF TEST----------------------------#

def main():
    pass
            
if __name__ == '__main__': 
    main()