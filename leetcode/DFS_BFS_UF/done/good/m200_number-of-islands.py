'''
https://leetcode.com/problems/number-of-islands
https://leetcode.com/articles/number-of-islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:


Input:
11110
11010
11000
00000

Output: 1


Example 2:


Input:
11000
11000
00100
00011

Output: 3
'''
class Solution(object):
	# sometimes dfs is faster than bfs(maintain the queue by ourself
	# deque here is much faster than normal list []
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        
        nIsland = 1
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    nIsland += 1
                    queue = [(x, y)]
                    
                    # exploreIsland
                    while len(queue) > 0:
                        i,j = queue.pop()
                        grid[i][j] = nIsland
                        
                        if i-1 >= 0 and grid[i-1][j] == '1':
                            queue.append((i-1, j))
                        if i+1 < len(grid) and grid[i+1][j] == '1':
                            queue.append((i+1, j))
                        if j-1 >= 0 and grid[i][j-1] == '1':
                            queue.append((i, j-1))
                        if j+1 < len(grid[0]) and grid[i][j+1] == '1':
                            queue.append((i, j+1))
        
        return nIsland - 1