'''
https://leetcode.com/problems/unique-paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:


Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right


Example 2:


Input: m = 7, n = 3
Output: 28
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        paths = [[0 for i in range(n)] for i in range(m)]

        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                paths[i][j] = (paths[i-1][j] if i > 0 else 0) + (paths[i][j-1] if j > 0 else 0)

        return paths[m-1][n-1]