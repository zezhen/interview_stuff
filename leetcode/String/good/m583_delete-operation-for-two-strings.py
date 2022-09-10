'''
https://leetcode.com/problems/delete-operation-for-two-strings/description/

similar to 
m161: one-edit-distance, scan once
h72: edit-distance, classical DP problem


Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
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
        
        # longest common subsequence
        dp = [[0 for _ in xrange(len(word1)+1)] for _ in xrange(len(word2)+1)]

        for i in xrange(1, len(word2)+1):
            for j in xrange(1,len(word1)+1):
              
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return len(word2) + len(word1) - 2 * dp[-1][-1]

s = Solution()
print s.minDistance("sea", "eat")