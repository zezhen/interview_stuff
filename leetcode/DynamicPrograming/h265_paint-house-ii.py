'''
https://leetcode.com/problems/paint-house-ii

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?
'''
import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0

        # dp[i][j] means the minimum cost of painting ith houses by using jth color
        # dp[i][j] = min(dp[i-1][k] + costs[i][j]), where k != j
        # min(dp[n][k]), 0<= k < m is the answer.
        n = len(costs)
        m = len(costs[0])
        dp = [[sys.maxint] * m for _ in xrange(n)]

        for j in xrange(m):
            dp[0][j] = costs[0][j]

        # pre-build the minimum index that minimize dp[i-1][k] + costs[i][j]
        minIndex = min(map(lambda (i,e):(e,i), enumerate(dp[0])))[1]
        secondIndex = min(map(lambda (i,e):(e,i) if i != minIndex else (sys.maxint, minIndex), enumerate(dp[0])))[1]

        for i in xrange(1, n):
            for j in xrange(m):
                if j != minIndex:
                    dp[i][j] = dp[i-1][minIndex] + costs[i][j]
                else:
                    dp[i][j] = dp[i-1][secondIndex] + costs[i][j]

            minIndex = min(map(lambda (i,e):(e,i), enumerate(dp[i])))[1]
            secondIndex = min(map(lambda (i,e):(e,i) if i != minIndex else (sys.maxint, minIndex), enumerate(dp[i])))[1]

        return min(dp[-1])

s = Solution()

print s.minCostII([[1,5,3],[2,9,4]]) == 5
print s.minCostII([[1,1,1],[1,1,1]]) == 2
print s.minCostII([[1,1,1],[0,0,0]]) == 1

print s.minCostII([[3,14,12,2,20,16,12,2],[9,6,9,8,2,9,20,18],[20,2,20,4,5,12,11,11],[16,3,7,5,15,2,2,4],[17,3,11,1,9,5,7,11]]) == 9