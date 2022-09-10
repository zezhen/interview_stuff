'''
https://leetcode.com/problems/the-maze-ii
https://leetcode.com/articles/the-maze-ii

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

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

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
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

Output: -1

Explanation: There is no way for the ball to stop at the destination.

https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''
import sys, collections
class Solution(object):
    # DFS solution is not ideal, refer to BFS solution https://leetcode.com/problems/the-maze-ii/discuss/98392/
    
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if start == destination: return 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = collections.defaultdict(lambda:[False]*4) # four direction
        row, col = len(maze), len(maze[0])

        # pre-check destination, if it's not at boundary, return -1
        x, y = destination
        for dr, dc in directions:
            nr, nc = x+dr, y+dc
            if nr < 0 or nr >= row or nc < 0 or nc >= col \
                    or maze[nr][nc] == 1:
                break
        else:
            return -1

        def search(start, row, col, steps):
            r, c = start
            ans = sys.maxint
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                # need move at least one step
                if nr < 0 or nr >= row or nc < 0 or nc >= col \
                    or maze[nr][nc] == 1 or visited[(r,c)][i]:
                    continue
                
                acc = steps + 1
                # check boundary then move
                while 0 <= nr + dr < row and 0 <= nc + dc < col and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc
                    acc += 1

                if [nr, nc] == destination:
                    return acc
                else:
                    # mark direction, then continue search
                    visited[(r,c)][i] = visited[(nr,nc)][i^1] = True
                    res = search((nr, nc), row, col, acc)
                    if res != -1:
                        ans = min(ans, res)
                    visited[(r,c)][i] = visited[(nr,nc)][i^1] = False
            
            return ans if ans != sys.maxint else -1
        
        return search(start, row, col, 0)


s = Solution()

# assert s.shortestDistance([[0]], [0,0], [0,0]) == 0
# assert s.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]) == 12
# assert s.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [0,1]) == 7
# assert s.shortestDistance([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], [0,4], [4,2]) == -1

print s.shortestDistance([[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]],[0,0],[8,6])