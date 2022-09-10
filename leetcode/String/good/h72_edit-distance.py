'''
https://leetcode.com/problems/edit-distance/description/

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1: return len(word2)
        if not word2: return len(word1)

        dp = [[0 for _ in xrange(len(word1)+1)] for _ in xrange(len(word2)+1)]

        # set boundaries
        for j in xrange(len(word1)+1):
            dp[0][j] = j
        for i in xrange(len(word2)+1):
            dp[i][0] = i

        # compare all elements n*n pairs, 
        # inherit mininum distance from three directions
        for i in xrange(1, len(word2)+1):
            for j in xrange(1, len(word1)+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]

s = Solution()
print s.minDistance("horse", "ros")
print s.minDistance("intention", "execution")
print s.minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically")