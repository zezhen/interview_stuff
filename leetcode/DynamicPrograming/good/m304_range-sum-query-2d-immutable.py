'''
https://leetcode.com/problems/range-sum-query-2d-immutable/description/

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

https://leetcode.com/static/images/courses/range_sum_query_2d.png

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 <= row2 and col1 <= col2.
'''

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
'''
1. maintain a matrix represent the accumulate area from (0,0) to (i,j), then
region((r1,c1), (r2,c2)) = acc[r2][c2] - acc[r2-1][c2] - acc[r2][c2-1] + acc[r1-1][c1-1]

2. how to get acc matrix?
acc[i][j] = matrix[i][j] + acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1]
'''






# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)