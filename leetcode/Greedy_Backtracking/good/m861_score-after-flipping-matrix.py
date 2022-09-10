'''
https://leetcode.com/problems/score-after-flipping-matrix
https://leetcode.com/articles/score-after-flipping-matrix
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 





Example 1:


Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

 

Note:


	1 <= A.length <= 20
	1 <= A[0].length <= 20
	A[i][j] is 0 or 1.


'''

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """


        # for row, if first number is 0, do toggling, otherwise not.
        # the weight on one column is same
        # if same numbers of 0 and 1, the toggle don't increase score
        # thus for each column, if # of 0 is more than 1, then do toggling
        
        if not A: return 0

        nRow, nCol = len(A), len(A[0])
        for row in A:
            if row[0] == 0:
                for c in xrange(nCol):
                    row[c] ^= 1

        for c in xrange(nCol):
            numberOf1 = sum(map(lambda t:t[c], A))
            if numberOf1 < nRow - numberOf1:
                for row in A: row[c] ^= 1

        score = 0
        for row in A:
            for i,n in enumerate(row):
                if n == 1:
                    score += 1 << (nCol - 1 - i)
        return score

s = Solution()
print s.matrixScore([[0]]) == 1
print s.matrixScore([[1]]) == 1
print s.matrixScore([[1],[1],[0]]) == 3
print s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]) == 39
print s.matrixScore([[0,0,0,0],[1,1,1,1],[1,1,1,1],[0,0,0,1]]) == 59
print s.matrixScore([[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0]]) == 92