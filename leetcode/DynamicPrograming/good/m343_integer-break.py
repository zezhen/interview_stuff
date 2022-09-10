'''
https://leetcode.com/problems/integer-break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:



Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 * 1 = 1.


Example 2:


Input: 10
Output: 36
Explanation:10 = 3+3+4,3*3*4=36
Note: You may assume that n is not less than 2 and not larger than 58.

'''

class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # condidering 2 <= n <= 58, we can use dp solution, if n is large, we need memo
        # dp[i] is the maximum product from i
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1
        # dp[i] = max(max(dp[j],j) * max(dp[i-j], i-j)), for j in [1, i/2+1]
        # max(dp[j],j) is the comparison of spliting or non-spliting j, we will choose a bigger one.
        
        dp = [0] * (n+1)
        dp[1] = dp[2] = 1
        for i in xrange(3, n+1):
            maxP = 0
            for j in xrange(1, i/2+1):
                maxP = max(maxP, max(j,dp[j]) * max(i-j,dp[i-j]))
            dp[i] = maxP

        return dp[-1]


    def integerBreak1(self, n):

        # might not be divided and must be divided
        product = [(0,0),(1,1)]
        if n <= 1:
            return product[n]

        for i in range(2, n + 1):
            _max = 0
            for j in range(1, i / 2 + 1):
                _max = max(product[j][0] * product[i - j][0], _max)
            product.append((max(_max, i), _max))

        return product[n][1]

s = Solution()
n = 
assert s.integerBreak1(n) == s.integerBreak1(n)