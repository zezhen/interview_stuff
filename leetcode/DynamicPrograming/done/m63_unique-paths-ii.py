'''
https://leetcode.com/problems/unique-paths-ii
https://leetcode.com/articles/unique-paths-ii
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:


Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0 for i in range(n)] for i in range(m)]

        paths[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = (paths[i-1][j] if i > 0 else 0) + (paths[i][j-1] if j > 0 else 0)

        return paths[m-1][n-1]