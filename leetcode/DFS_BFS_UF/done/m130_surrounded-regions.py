'''
https://leetcode.com/problems/surrounded-regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:


X X X X
X O O X
X X O X
X O X X


After running your function, the board should be:


X X X X
X X X X
X X X X
X O X X


Explanation:

Surrounded regions shouldn't be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

import collections
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        
        row, col = len(board), len(board[0])
        surrounded = collections.defaultdict(dict)

        # dfs mark all connected node as surrounded=False
        def break_out(i, j):
            surrounded[i][j] = False
            if i > 0 and board[i-1][j] == 'O' and surrounded[i-1][j]:
                break_out(i-1, j)
            if j > 0 and board[i][j-1] == 'O' and surrounded[i][j-1]:
                break_out(i, j-1)
            if i < row-1 and board[i+1][j] == 'O' and surrounded[i+1][j]:
                break_out(i+1, j)
            if j < col-1 and board[i][j+1] == 'O' and surrounded[i][j+1]:
                break_out(i, j+1)

        # initial all 'O' as surrounded=True
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == 'O': surrounded[i][j] = True

        # start from boundary, if 'O' in boundary, it's a breakthrough
        for r in xrange(row):
            if board[r][0] == 'O' and surrounded[r][0]:
                break_out(r, 0)
            if board[r][col-1] == 'O' and surrounded[r][col-1]:
                break_out(r, col-1)
        for c in xrange(col):
            if board[0][c] == 'O' and surrounded[0][c]:
                break_out(0, c)
            if board[row-1][c] == 'O' and surrounded[row-1][c]:
                break_out(row-1, c)

        # change all none surrounded 'O' to 'X'
        for r,cols in surrounded.iteritems():
            for c,sur in cols.iteritems():
                if sur: board[r][c] = 'X'


s = Solution()
# board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
board = [["O","O"],["O","O"]]
print board
s.solve(board)
print board
        
