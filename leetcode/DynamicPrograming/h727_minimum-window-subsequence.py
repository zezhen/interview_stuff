'''
https://leetcode.com/problems/minimum-window-subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
'''
import sys
import bisect
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # dp[i][j] means the minWindow(S[i:], T[j:]), where S[i] = T[j]
        # dp[i][j] = min(dp[k][j+1] + (k-i)), where k > i and S[k] = T[j+1]
        # min(dp[*][0]) is the answer

        N, M = len(S), len(T)
        dp = [[sys.maxint]*M for _ in xrange(N)]
        lastIndex = [-1] * N

        prev = []
        for i in xrange(N):
            if S[i] == T[M-1]:
                dp[i][M-1] = 1
                lastIndex[i] = i
                prev.append(i)

        for j in range(M-1)[::-1]:
            cur = []
            for i in xrange(N):
                if S[i] != T[j]: continue
                k = bisect.bisect(prev, i)
                # print prev, i, prev[k], k < len(prev), dp[prev[k]][j+1], dp[i][j]
                if k < len(prev):
                    dp[i][j] = min(dp[i][j], prev[k] - i + dp[prev[k]][j+1])
                    lastIndex[i] = lastIndex[prev[k]]
                # print dp[i][j]
                cur.append(i)
            prev = cur
        
        ans, minLen = '', N - 1
        for i in xrange(N):
            if dp[i][0] != sys.maxint and lastIndex[i] + 1 - i < minLen:
                ans = S[i:lastIndex[i]+1]
                minLen = len(ans)
        return ans

s = Solution()
print s.minWindow("", "bde")
print s.minWindow("abcdebdde", "bde")
print s.minWindow("bbbbbbbbbbccccde", "bde")
print s.minWindow("bbbbcdeeeeeeeee", "bde")
print s.minWindow("bbbbcdeeeeeeeee", "bbbbde")
print s.minWindow("bbbbccccccddddddeeeeeeeee", "bbbbde")

