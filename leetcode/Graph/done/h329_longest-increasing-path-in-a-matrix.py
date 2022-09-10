'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix
https://leetcode.com/articles/longest-increasing-path-matrix
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:


Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].


Example 2:


Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        longestPath = [[-1 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        self.ans = 0

        def search(matrix, longestPath, i, j):
            if longestPath[i][j] != -1:
                return longestPath[i][j]

            val = matrix[i][j]
            longest = 1
            if i > 0 and matrix[i-1][j] > val:
                longest = max(longest, search(matrix, longestPath, i-1, j) + 1)
            if j > 0 and matrix[i][j-1] > val:
                longest = max(longest, search(matrix, longestPath, i, j-1) + 1)
            if i < len(matrix) - 1 and matrix[i+1][j] > val:
                longest = max(longest, search(matrix, longestPath, i+1, j) + 1)
            if j < len(matrix[0]) - 1 and matrix[i][j+1] > val:
                longest = max(longest, search(matrix, longestPath, i, j+1) + 1)

            longestPath[i][j] = longest
            self.ans = max(self.ans, longest)
            return longest

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if longestPath[i][j] == -1:
                    search(matrix, longestPath, i, j)

        return self.ans

s = Solution()

print s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
print s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]] )