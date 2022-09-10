'''
https://leetcode.com/problems/search-a-2d-matrix/description/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

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
        
        i = bisect.bisect(map(lambda arr:arr[0], matrix), target) - 1
        
        if i >= len(matrix):
            i = len(matrix) - 1
            
        j = bisect.bisect_left(matrix[i], target)
        return j < len(matrix[i]) and matrix[i][j] == target