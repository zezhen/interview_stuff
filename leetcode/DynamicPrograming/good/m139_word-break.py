'''
https://leetcode.com/problems/word-break/description/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution(object):
    '''
    my first response it greedy + backtracking, 
    while later after use dp is truly a dp problem
    then writing the backtracking solution, we definitely need
    to use memo, which is another form of dp
    '''
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.wordBreak_memo(s, wordDict)

    def wordBreak_memo(self, s, wordDict):
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        
        memo = {}
        def search(l, r):
            if l in memo: return memo[l]
            if l >= r: return True
            for j in xrange(l, r):
                if s[l:j+1] in wordSet and search(j+1, r): 
                    memo[l] = True
                    return True
            return False
        
        return search(0, len(s))

    def wordBreak_dp(self, s, wordDict):
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)

        dp = [False] * len(s)

        for i in xrange(len(s)):
            for j in xrange(i,-1,-1):
                if s[j:i+1] in wordSet and (j <= 0 or dp[j-1]):
                    dp[i] = True
                    break

        return dp[-1]

s = Solution()
assert s.wordBreak("abc", ["leet", "code"]) == False
assert s.wordBreak("leet", ["leet", "abc"]) == True
assert s.wordBreak("leetcode", ["leet", "code"]) == True
assert s.wordBreak("applepenapple", ["apple", "pen"]) == True
assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
