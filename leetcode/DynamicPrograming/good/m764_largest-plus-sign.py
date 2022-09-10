'''
https://leetcode.com/problems/largest-plus-sign/description/

In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
Note:

N will be an integer in the range [1, 500].
mines will have length at most 5000.
mines[i] will be length 2 and consist of integers in the range [0, N-1].
(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
'''

class Solution(object):
	# my solution is use dp to solve the problem
	# bs solution use least time, which look at mine directly
	# use binary to check the boundary of left/right and up/down.
    def orderOfLargestPlusSign(self, N, mines):
        return self.orderOfLargestPlusSign_bs(N, mines)

    def orderOfLargestPlusSign_dp(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """

        # four direction, left, right, up, down
        dp = [[[1,1,1,1] for _ in xrange(N)] for _ in xrange(N)]
        for mine in mines:
            dp[mine[0]][mine[1]] = [0,0,0,0]
        # print dp

        for i in xrange(1, N-1):
            for j in xrange(1, N-1):
                if dp[i][j][0] > 0:
                    dp[i][j][0] = dp[i][j-1][0] + 1
                    dp[i][j][2] = dp[i-1][j][2] + 1
        # print dp

        for i in xrange(N-2, 0, -1):
            for j in xrange(N-2, 0, -1):
                if dp[i][j][1] > 0:
                    dp[i][j][1] = dp[i][j+1][1] + 1
                    dp[i][j][3] = dp[i+1][j][3] + 1
        # print dp
        return max(map(lambda row: max(map(lambda t:min(t), row)), dp))

    def orderOfLargestPlusSign_bs(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        import bisect
        rows = [[-1, N] for _ in xrange(N)]
        cols = [[-1, N] for _ in xrange(N)]
        for r, c in mines:
            rows[r].append(c); cols[c].append(r)
        for i in xrange(N):
            rows[i].sort()
            cols[i].sort()
        print rows
        print cols
        mxp = 0
        for r in xrange(N):
            for i in xrange(len(rows[r])-1):
                left_b = rows[r][i]
                right_b = rows[r][i+1]
                for c in xrange(left_b+mxp+1, right_b-mxp):
                    idx = bisect.bisect_right(cols[c], r)-1
                    up_b = cols[c][idx]
                    down_b = cols[c][idx+1]
                    mxp = max(mxp, min(c-left_b, right_b-c, r-up_b, down_b-r))
                    print r, i, c, left_b, right_b, up_b, down_b, mxp
        return mxp

s = Solution()

# assert s.orderOfLargestPlusSign(1, [[0,0]]) == 0
# assert s.orderOfLargestPlusSign(2, []) == 1
assert s.orderOfLargestPlusSign(5, [[4,2]]) == 2
# assert s.orderOfLargestPlusSign(5, [[3,1],[1,3]]) == 3
# assert s.orderOfLargestPlusSign(5, [[3,1]]) == 3
# assert s.orderOfLargestPlusSign(5, [[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0],[2,1],[2,3],[2,4],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[4,4]]) == 1