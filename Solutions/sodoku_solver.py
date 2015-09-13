#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Sudoku Solver] in LeetCode.

Created on: Nov 27, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.dfs(board)

    def dfs(self, board):
        for x in range(9):
            for y in range(9):
                if self.board[x][y] =='.':
                    for i in '123456789':
                        self.board[x][y] = i
                        if self.is_valid(x, y) and self.dfs(self.board):    #important
                            return True
                        self.board[x][y] = '.'
                    return False
        return True

    def is_valid(self, x, y):
        tmp=self.board[x][y]
        self.board[x][y]='D'
        for i in range(9):
            if self.board[i][y]==tmp:
                return False
        for i in range(9):
            if self.board[x][i]==tmp:
                return False
        for i in range(3):
            for j in range(3):
                if self.board[(x/3)*3+i][(y/3)*3+j]==tmp:
                    return False
        self.board[x][y]=tmp
        return True

#----------------------------SELF TEST----------------------------#

def main():
    board=[list("53..7...."),
           list("6..195..."),
           list(".98....6."),
           list("8...6...3"),
           list("4..8.3..1"),
           list("7...2...6"),
           list(".6....28."),
           list("...419..5"),
           list("....8..79")]

    solution = Solution()
    solution.solveSudoku(board)
    for i in range(len(board)):
        print board[i]
            
if __name__ == '__main__': 
    main()