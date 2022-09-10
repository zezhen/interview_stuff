'''
https://leetcode.com/problems/distinct-subsequences/description/

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''
import bisect
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t: return 0

        # dp[i][j] means the subsequence number of (S[i:], T[j:]), where S[i] = T[j]
        # dp[i][j] = min(dp[k][j+1]), where k > i and S[k] = T[j+1]
        # min(dp[*][0]) is the answer
        n, m = len(s), len(t)
        dp = [[0] * len(t) for _ in xrange(len(s))]

        prev = []
        for i in xrange(n):
            if s[i] == t[m-1]:
                dp[i][m-1] = 1
                prev.append(i)

        for j in range(m-1)[::-1]:
            tmp = []
            for i in xrange(n):
                if s[i] != t[j]: continue
                tmp.append(i)
                k = bisect.bisect(prev, i)
                for x in xrange(k, len(prev)):
                    dp[i][j] += dp[prev[x]][j+1]
                    # print i, j, prev[x], j+1, dp[i][j], dp[prev[x]][j+1]
            prev = tmp

        ans = 0
        for i in xrange(n):
            ans += dp[i][0]
        return ans

s = Solution()
print s.numDistinct("rabbbit", "rabbit")
print s.numDistinct("babgbag", "bag")
print s.numDistinct("babgbag", "")
print s.numDistinct("", "abc")
print s.numDistinct("a", "a")
