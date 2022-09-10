'''
https://leetcode.com/problems/spiral-matrix
https://leetcode.com/articles/spiral-matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:


Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        order = [ ]
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n == 1:
            return [matrix[0][0]]


        x, y, count = 0, 0, 0
        
        index, direction = 0, [[0,1,n-1],[1,0,m-1],[0,-1,n-1],[-1, 0, m-1]]
        print m, n
        for v in xrange(m * n):
            
            if direction[index][2] <= 0:
                index += 1

            order.append(matrix[x][y])
            x += direction[index][0]
            y += direction[index][1]

            count += 1
            if count == direction[index][2]:
                direction[index][2] -= 2
                index += 1
                count = 0
                if index == 4:
                    index = 0
                    
                    x += 1
                    y += 1
        return order