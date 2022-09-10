'''
https://leetcode.com/problems/the-maze
https://leetcode.com/articles/the-maze

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.
https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png
 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''
import collections
class Solution(object):
    # mine is dfs solution, bfs refer to https://leetcode.com/problems/the-maze/discuss/97071
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """

        if start == destination: return True

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = collections.defaultdict(lambda:[False]*4) # four direction
        row, col = len(maze), len(maze[0])

        # pre-check destination, if it's not at boundary, return False
        x, y = destination
        for dr, dc in directions:
            nr, nc = x+dr, y+dc
            if nr < 0 or nr >= row or nc < 0 or nc >= col \
                    or maze[nr][nc] == 1:
                break
        else:
            return False

        def search(start, row, col):
            r, c = start
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                # need move at least one step
                if nr < 0 or nr >= row or nc < 0 or nc >= col \
                    or maze[nr][nc] == 1 or visited[(r,c)][i]:
                    continue

                # mark searched direction, then move and check boundary
                visited[(r,c)][i] = True
                while 0 <= nr + dr < row and 0 <= nc + dc < col and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc

                if [nr, nc] == destination:
                    return True
                else:
                    # mark reverse direction, then continue search
                    visited[(nr,nc)][i^1] = True
                    res = search((nr, nc), row, col)
                    if res: return res
            return False

        return search(start, row, col)


s = Solution()
print s.hasPath([[0]], [0,0], [0,0]) == True
print s.hasPath([[0]], [0,0], [0,0]) == True
print s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]) == True
print s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [0,1]) == True
print s.hasPath([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], [0,4], [4,2]) == False
