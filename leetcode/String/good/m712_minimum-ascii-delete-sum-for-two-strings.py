'''
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
'''

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
        '''
        dp[i][j] is the cost for s1.substr(0,i) and s2.substr(0, j). Note s1[i], s2[j] not included in the substring.

        Base case: dp[0][0] = 0
        target: dp[m][n]

        if s1[i-1] = s2[j-1]   // no deletion
            dp[i][j] = dp[i-1][j-1];
        else   // delete either s1[i-1] or s2[j-1]
            dp[i][j] = min(dp[i-1][j]+s1[i-1], dp[i][j-1]+s2[j-1]);
        '''

        if not s1: return sum(map(ord, s2))
        if not s2: return sum(map(ord, s1))
        
        dp = [[0 for _ in xrange(len(s1)+1)] for _ in xrange(len(s2)+1)]
        for j in xrange(1, len(s1)+1):
            dp[0][j] = dp[0][j-1] + ord(s1[j-1])
        for i in xrange(1, len(s2)+1):
            dp[i][0] = dp[i-1][0]+ord(s2[i-1])
            for j in xrange(1,len(s1)+1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1] + ord(s1[j-1]), dp[i-1][j] + ord(s2[i-1]))

        return dp[-1][-1]

s = Solution()
print s.minimumDeleteSum("", "eat")
print s.minimumDeleteSum("sea", "eat")
print s.minimumDeleteSum("delete", "leet")
print s.minimumDeleteSum("a", "at")