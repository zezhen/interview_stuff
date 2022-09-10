'''
https://leetcode.com/problems/knight-probability-in-chessboard/description/

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

 https://assets.leetcode.com/uploads/2018/10/12/knight.png



 

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 

Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.

'''

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        memo = {}

        def jump(i, j, x):
            if (i, j, x) in memo:
                return memo[(i, j, x)]

            if i < 0 or i >= N or j < 0 or j >= N: return 1.0
            if x == 0: return 0.0

            out = 0
            for o in [jump(i-2, j+1, x-1), jump(i-2, j-1, x-1), jump(i-1, j+2, x-1), jump(i-1, j-2, x-1), \
                jump(i+2, j+1, x-1), jump(i+2, j-1, x-1), jump(i+1, j+2, x-1), jump(i+1, j-2, x-1)]:
                out += 1.0 / 8 * o

            memo[(i,j,x)] = out
            return out

        return 1 - jump(r, c, K)

s = Solution()
assert s.knightProbability(10, 0, 0, 0) == 1
assert s.knightProbability(1, 1, 0, 0) == 0
assert s.knightProbability(10, 1, 9, 9) == 0.25
assert s.knightProbability(10, 1, 0, 9) == 0.25
assert s.knightProbability(3, 2, 0, 0) == 0.0625

s.knightProbability(25, 100, 12, 12)