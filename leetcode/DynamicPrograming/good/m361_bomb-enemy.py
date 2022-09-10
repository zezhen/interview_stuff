'''
https://leetcode.com/problems/bomb-enemy/description/

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
'''

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

'''
the key point of DP is how to reduce the duplicated lookup

for (i,j), we can lookup 4 direction, if we already know the numbers kill in 4 adjacent cell in diff directions, we can easily get the final number. thus, we need to maintain 4 directions emenies kill numbers for each cell.

e.g. left direction

start position or stop condition:
left[i][0] = 1 if grid[i][0] == 'E' else 0
left[i][j] = 0 if grid[i-1][j] == 'W' else
				left[i-1][j] + (1 if grid[i-1][j] == 'E' else 0)
same for other directions.
'''