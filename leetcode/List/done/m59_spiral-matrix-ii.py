'''
https://leetcode.com/problems/spiral-matrix-ii
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:


Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [ [ 0 for i in range(n) ] for i in range(n) ]
        
        x, y, count, _len = 0, 0, 0, n - 1
        index, direction = 0, [(0,1),(1,0),(0,-1),(-1, 0)]
        
        for v in xrange(1, n*n + 1):
            matrix[x][y] = v
            x += direction[index][0]
            y += direction[index][1]

            count += 1
            if count == _len:
                index += 1
                count = 0
                if index == 4:
                    index = 0
                    _len -= 2
                    x += 1
                    y += 1
        return matrix
           