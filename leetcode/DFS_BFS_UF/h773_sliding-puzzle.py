'''
https://leetcode.com/problems/sliding-puzzle
https://leetcode.com/articles/sliding-puzzle
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.



Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.



Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]



Input: board = [[3,2,4],[1,5,0]]
Output: 14


Note:


	board will be a 2 x 3 array as described above.
	board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

'''

import heapq
from copy import copy, deepcopy
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def encode(board):
            hashcode, base = 0, 1
            for row in board:
                for e in row:
                    hashcode += e * base
                    base *= 10
            return hashcode

        target = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1)} # need add 0 here?
        def scan(board):
            dis = emptyX = emptyY = 0
            for x, row in enumerate(board):
                for y, e in enumerate(row):
                    if e == 0: 
                        emptyX = x
                        emptyY = y
                        continue
                    targetX, targetY = target[e]
                    dis += abs(targetX - x) + abs(targetY - y)
            return emptyX, emptyY, dis

        visited = set()
        emptyX, emptyY, dis = scan(board)
        queue = [(0, dis, emptyX, emptyY, board)]
        visited.add(encode(board))

        dirs = [(0, 1), (1,0), (0, -1), (-1, 0)]
        while queue:
            move, dis, emptyX, emptyY, board = heapq.heappop(queue)
            if dis == 0: return move

            for dx, dy in dirs:
                x, y = emptyX + dx, emptyY + dy
                if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]): continue
                new_board = deepcopy(board)
                new_board[x][y], new_board[emptyX][emptyY] = 0, new_board[x][y]

                code = encode(new_board)
                if code in visited:
                    continue
                
                _, _, dis = scan(new_board)
                queue.append((move+1, dis, x, y, new_board))
                visited.add(code)

        return -1


s = Solution()
print s.slidingPuzzle([[1,2,3],[4,0,5]]) == 1
print s.slidingPuzzle([[1,2,3],[5,4,0]]) == -1
print s.slidingPuzzle([[4,1,2],[5,0,3]]) == 5
print s.slidingPuzzle([[3,2,4],[1,5,0]]) == 14




