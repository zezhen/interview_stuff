'''
https://leetcode.com/problems/making-a-large-island
https://leetcode.com/articles/making-a-large-island
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:


Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.


Example 2:


Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:


Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

 

Notes:


	1 <= grid.length = grid[0].length <= 50.
	0 <= grid[i][j] <= 1.


 
'''
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        
        gid = 0
        group_count = []
        row, col = len(grid), len(grid[0])
        group = [[-1 for _ in xrange(col)] for _ in xrange(row)]
        
        def grouping(i, j, gid):
            group[i][j] = gid
            count = 1
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ti, tj = i + di, j + dj
                if ti < 0 or ti >= row or tj < 0 or tj >= col or grid[ti][tj] != 1 or group[ti][tj] != -1:
                    continue
                count += grouping(ti, tj, gid)
            return count
        
        for i in xrange(row):
            for j in xrange(col):
                if group[i][j] == -1 and grid[i][j] == 1:
                    group_count.append(grouping(i, j, gid))
                    gid += 1
        
        ans = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] != 0: continue
                
                adja_group = set()
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ti, tj = i + di, j + dj
                    if ti < 0 or ti >= row or tj < 0 or tj >= col or grid[ti][tj] != 1:
                        continue
                    adja_group.add(group[ti][tj])
                count = 1
                for gid in adja_group:
                    count += group_count[gid]
                ans = max(ans, count)
        
        return ans if ans > 0 else row * col

s = Solution()
print s.largestIsland([[]]) == 0
print s.largestIsland([[0, 0], [0, 0]]) == 1
print s.largestIsland([[1, 0], [0, 1]]) == 3
print s.largestIsland([[1, 1], [1, 0]]) == 4
print s.largestIsland([[1, 1], [1, 1]]) == 4