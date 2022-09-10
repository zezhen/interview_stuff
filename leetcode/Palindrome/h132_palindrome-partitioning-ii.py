'''
https://leetcode.com/problems/palindrome-partitioning-ii/description/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.


'''

import collections
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        # cut[i] is the minimum of cut[j - 1] + 1 (j <= i), if [j, i] is palindrome.
        # If [j, i] is palindrome, [j + 1, i - 1] is palindrome, and c[j] == c[i].
        # refer to https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42213

        if not s: return 0
        n = len(s)
        cut = [0] * n
        pal = set()

        for i in xrange(n):
            _min = i
            for j in xrange(i+1):
                if s[i] == s[j] and (j + 1 > i - 1 or (j+1,i-1) in pal):
                    pal.add((j, i))
                    _min = 0 if j == 0 else min(_min, cut[j-1]+1)
            cut[i] = _min
        # print cut, pal
        return cut[-1]

s = Solution()
print s.minCut("") == 0
print s.minCut("ab") == 1
print s.minCut("aba") == 0
print s.minCut("abac") == 1