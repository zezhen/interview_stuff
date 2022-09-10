'''
https://leetcode.com/problems/perfect-squares/description/

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

import sys, math
class Solution(object):
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # refer to http://www.cnblogs.com/grandyang/p/4800552.html
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
            
        a = 0
        while a * a < n:
            b = int(math.sqrt(n - a * a))
            if a*a + b*b == n:
                return 2 if a*b > 0 else 1
            a += 1
        
        return 3

    def numSquares_dp(self, n):
        dp = [sys.maxint] * (n+1)
        dp[0] = 0
        for i in xrange(0,n+1):
            j = 1
            while i + j*j <= n:
                dp[i+j*j] = min(dp[i+j*j], dp[i] + 1)
                j += 1
        # print dp
        return dp[n]

s = Solution()

for i in xrange(10, 100):
    assert s.numSquares(i) == s.numSquares_dp(i)