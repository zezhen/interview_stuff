'''
https://leetcode.com/problems/find-and-replace-pattern/description/

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
'''

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        letter2pos = {}
        for i,c in enumerate(pattern):
            if c not in letter2pos: letter2pos[c] = []
            letter2pos[c].append(i)

        ans = []
        for word in words:
            if len(word) != len(pattern): continue
            match, letterSet = True, set()
            for poslist in letter2pos.values():
                c = word[poslist[0]]
                letterSet.add(c)
                for i in range(1, len(poslist)):
                    if c != word[poslist[i]]: 
                        match = False
                        break
            if match and len(letterSet) == len(letter2pos):
                ans.append(word)

        return ans

s = Solution()
assert s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb") == ['mee', 'aqq']
assert s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc","abcd"], "xyz") == ['abc', 'deq']
assert s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc","abcd"], "aa") == []
assert s.findAndReplacePattern(["abc"], "aa") == []



