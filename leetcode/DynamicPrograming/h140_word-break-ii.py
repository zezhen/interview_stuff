'''
https://leetcode.com/problems/word-break-ii/description/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        wordSet = set()
        maxLen = 0
        for word in wordDict:
            wordSet.add(word)
            maxLen = max(maxLen, len(word))
        
        ans = []
        memo = {}
        def search(l):
            if l in memo: return memo[l]
            if l >= len(s): return [""]

            memo[l] = set()
            for j in xrange(l, l+maxLen):
                if s[l:j+1] in wordSet:
                    res = search(j+1)
                    # print l, s[l:j+1], res
                    for substr in res:
                        strl = s[l:j+1] + (" " + substr if substr !="" else "")
                        if l == 0:
                            ans.append(strl)
                        else:
                            memo[l].add(strl)
            return memo[l]
        
        search(0)
        return ans

s = Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
print s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])

import random
lines = open('/Users/zezhen/Downloads/words.txt').readlines()

wordDict = set()
sentence = []
for i in xrange(30):
    line = random.choice(lines)
    if "'" in line or "-" in line: continue
    wordDict.add(line.strip())
    if random.randint(0,10) > 0.7:
        sentence.append(line.strip())

print "".join(sentence)
print list(wordDict)
# print s.wordBreak("".join(sentence), wordDict)


