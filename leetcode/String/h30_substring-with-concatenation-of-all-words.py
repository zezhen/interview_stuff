'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
'''

import collections
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        counter = collections.Counter()
        size = 0
        for word in words:
            counter.update(word)
            size += len(word)

        if len(s) < size: return []

        wordSet = set(words)
        wlen = len(words[0])

        def verifyWord(ss):
            for i in xrange(0,len(ss)-wlen, wlen):
                if ss[i:i+wlen] not in wordSet:
                    return False
            return True


        ans = []
        i = 0
        # or use int counter 
        acc = collections.Counter(s[:size])
        while i < len(s) - size:
            if acc == counter and verifyWord(s[i:i+size]):
                ans.append(i)
            
            acc.update({s[i]:-1})
            acc.update({s[i+size]:1})
            i += 1

        return ans

s = Solution()
print s.findSubstring('barfoothefoobarman', ['bar', 'foo'])