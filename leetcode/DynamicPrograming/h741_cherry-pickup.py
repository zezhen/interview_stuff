'''
https://leetcode.com/problems/cherry-pickup/description/

In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
'''
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        N = len(grid)
        M = (N << 1) - 1

        dp = [[0] * N for _ in xrange(N)]
        for n in xrange(M):
            for i in range(N)[::-1]:   # start from end won't overwrite preivous data
                for p in range(N)[::-1]:
                    j, q = n-i, n-p

                    if j < 0 or j >= N or q < 0 or q >= N or grid[i][j] < 0 or grid[p][q] < 0:
                        dp[i][p] = -1
                        continue

                    if i > 0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p])
                    if p > 0:
                        dp[i][p] = max(dp[i][p], dp[i][p-1])
                    if i > 0 and p > 0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p-1])

                    if dp[i][p] >= 0:
                        dp[i][p] += grid[i][j]
                        if i != p:
                            dp[i][p] += grid[p][q]
        return max(dp[N-1][N-1], 0)

s = Solution()
print s.cherryPickup([[0, 1, -1],[1, 0, -1],[1, 1,  1]])