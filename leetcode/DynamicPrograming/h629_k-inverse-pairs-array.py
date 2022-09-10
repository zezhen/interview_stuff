'''
https://leetcode.com/problems/k-inverse-pairs-array/description/

Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 109 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: 
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
Example 2:
Input: n = 3, k = 1
Output: 2
Explanation: 
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
Note:
The integer n is in the range [1, 1000] and k is in the range [0, 1000].
'''

class Solution(object):
    '''
    given number n, we can get array [1,2,3,4,...,n]
    to generate pair(n, k), we need some way to convert it to subproblem pair(n-i, k-j)

    if we move i to the head of array, new array will become [i, 1,2,3,...,i-1,i+1,...,n]
    for this new array, we already get i-1 inverse pair, aka (1,i), (2,i), ..., (i-1,i)
    so the problem become find k-i inverse pair in n-1 array

    first tried BT+memo but timeout, switch to DP solution
    '''


    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7
        dp = [[0]*(k+1) for _ in xrange(n+1)]

        for i in xrange(1,n+1):
            dp[i][0] = 1
            if k > 0:
                dp[i][1] = i - 1

        for i in xrange(1,n+1):
            acc = dp[i-1][0]
            if k > 0:
                acc += dp[i-1][1]
            for j in xrange(2,k+1):
                if j > (i-1)*i/2: break
                acc += dp[i-1][j]
                if j >= i:
                    acc -= dp[i-1][j-i]
                dp[i][j] = acc % mod

        return dp[-1][-1]

    memo = {}
    def kInversePairs_dfs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if k > n * (n - 1) / 2: return 0
        if k == 0: return 1
        if k == 1: return n - 1
        
        if (n, k) in self.memo: 
            return self.memo[(n,k)]

        mod = 10**9 + 7
        ans = 0
        for i in range(n):
            if i > k: break
            r = self.kInversePairs(n-1, k-i)
            # print n-1, k-i, r
            ans += r
        self.memo[(n,k)] = (ans % mod)
        return self.memo[(n,k)]



s = Solution()
print s.kInversePairs(3,0) == 1
print s.kInversePairs(3,1) == 2
print s.kInversePairs(3,2) == 2
print s.kInversePairs(3,3) == 1
print s.kInversePairs(4,5) == 3
print s.kInversePairs(10,5) == 1068
print s.kInversePairs(100,5) == 87369546
print s.kInversePairs(1000,500) == 955735232