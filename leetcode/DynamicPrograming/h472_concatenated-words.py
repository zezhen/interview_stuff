'''
https://leetcode.com/problems/concatenated-words

Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";  "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".



Note:

The number of elements of the given array will not exceed 10,000 
The length sum of elements in the given array will not exceed 600,000. 
All the input string will only include lower case letters.
The returned elements order does not matter. 

'''

class Solution(object):
    '''
    1. same like word-break, maintain a word directory, use dp to check every word one by one.
    2. order words by their length in desc order, build the trie tree, for word w, check through the trie tree, if node contains 'word', it means prefix is a word, (there is no duplicates, don't need count for words number), we need to choose continue current path down or restart from root, thus we need a candidate nodes queue for next step, start can be always be root. what's the complexity? 
        comment: tried but more complicated, there is no reuse of scanned part
    '''       

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # using dp solution costs 1020 ms in total
        # using simple recurrence solution costs only 180 ms, 
        # that tell us to use library or built-in function is a better solution
        return self.findAllConcatenatedWordsInADict_rec(words)

    def findAllConcatenatedWordsInADict_rec(self, words):
        def helper(words_set, word, conca):
            if conca and word in words_set:
                return True
            for idx in xrange(1, len(word)):
                if word[:idx] in words_set and helper(words_set, word[idx:], True):
                    return True
            return False

        words_set = set(words)
        res = []
        for word in words:
            if helper(words_set, word, False):
                res.append(word)
        return res


    def findAllConcatenatedWordsInADict_dp(self, words):
        wordSet = set()
        for word in words:
            wordSet.add(word)

        def search(s):
            dp = [False] * len(s)
            for i in xrange(len(s)):
                for j in xrange(i,-1,-1):
                    if s[j:i+1] in wordSet and (j <= 0 or dp[j-1]) and not (j==0 and i == len(s)-1):
                        dp[i] = True
                        break
            return dp[-1]

        ans = []
        for word in words:
            if search(word): ans.append(word)
        return ans

s = Solution()
assert s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) == ['catsdogcats', 'dogcatsdog', 'ratcatdogcat']
assert s.findAllConcatenatedWordsInADict(["aa","b","c","aaaa","bc","ab"]) == ['aaaa', 'bc']

# import random
# lines = open('/Users/zezhen/Downloads/words.txt').readlines()

# wordDict = set()
# for i in xrange(10000):
#     word1 = random.choice(lines).strip()
#     word2 = random.choice(lines).strip()
#     if "'" in word1 or "-" in word1: continue
#     if "'" in word2 or "-" in word2: continue
#     wordDict.add(word1)
#     wordDict.add(word2)
#     if random.randint(0,10) > 0.7:
#         wordDict.add(word1 + word2)

# print list(wordDict)
# print s.wordBreak("".join(sentence), wordDict)





