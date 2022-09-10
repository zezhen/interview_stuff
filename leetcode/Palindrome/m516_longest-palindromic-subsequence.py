'''
https://leetcode.com/problems/longest-palindromic-subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.


Example 1:
Input: 

"bbbab"

Output: 

4

One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:

"cbbd"

Output:

2

One possible longest palindromic subsequence is "bb".
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dp = [[0 for _ in xrange(len(s))] for _ in xrange(len(s))]

        for i in xrange(len(s)-1,-1,-1):
            dp[i][i] = 1
            for j in xrange(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][-1]

s = Solution()
print s.longestPalindromeSubseq("bbbab") == 4
print s.longestPalindromeSubseq("cbbd") == 2
print s.longestPalindromeSubseq("aaa") == 3

