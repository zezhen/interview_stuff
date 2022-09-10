'''
https://leetcode.com/problems/maximal-square/description/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        # dp[i][j] means the maximal square size, whose bottle-right locate at (i,j)
        # dp[0][0] = matrix[0][0] == 1
        # dp[i][j] = 0 if matrix[i][j] == 0 else min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + matrix[i][j]