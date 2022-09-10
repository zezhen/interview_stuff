'''
https://leetcode.com/problems/search-a-2d-matrix-ii/description/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

'''

import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)

        while l <= r and t <= b:

            if l < r:
                r = bisect.bisect(matrix[t], target) - 1
            if matrix[t][r] == target:
                return True

            if t < b:
                b = bisect.bisect(map(lambda arr:arr[l], matrix), target) - 1
            if matrix[b][l] == target:
                return True

            l += 1
            t += 1
        
        return False