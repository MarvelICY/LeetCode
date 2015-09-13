#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction:
Solution of [Valid Sudoku] in LeetCode.

Created on: Nov 10, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    # hash table
    # square 9:00-22;row 9:91-99;column 9:81-89
    # encode: position+digit--011
    def isValidSudoku(self, board):
        dict = {}
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col] != '.':
                    row_key = 900 + row * 10 + int(board[row][col])  
                    col_key = 800 + col * 10 + int(board[row][col]) 
                    sqr_key = row / 3 * 100 + col / 3 * 10 + int(board[row][col])
                    if row_key not in dict and col_key not in dict and sqr_key not in dict:
                        dict[row_key] = 1
                        dict[col_key] = 1
                        dict[sqr_key] = 1
                    else:
                        return False
        return True 
        

        
#----------------------------SELF TEST----------------------------#

def main():
    test_board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    #test_board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
    solution = Solution()
    print solution.isValidSudoku(test_board)
    pass
            
if __name__ == '__main__': 
    main()