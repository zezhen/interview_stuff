'''
https://leetcode.com/problems/word-squares

Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 <= k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:

There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
'''
import collections
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        

        prefixCache = collections.defaultdict(list)
        for i, w in enumerate(words):
            for k in xrange(1, len(w)):
                prefixCache[w[:k]].append(w)
        ans = []

        def dfs(square, level):
            if level == len(square):
                ans.append(square[:])
                return

            prefix = []
            for i in xrange(level):
              prefix.append(square[i][level])
            prefix = ''.join(prefix)
            if prefix not in prefixCache: return
            for cand in prefixCache[prefix]:
                square[level] = cand
                dfs(square, level + 1)

        wlen = len(words[0])
        for i, w in enumerate(words):
            square = [''] * wlen
            square[0] = w
            dfs(square, 1)

        return ans

s = Solution()
print s.wordSquares(["area","lead","wall","lady","ball"])
print s.wordSquares(["abat","baba","atan","atal"])
print s.wordSquares(["aaaa"])
