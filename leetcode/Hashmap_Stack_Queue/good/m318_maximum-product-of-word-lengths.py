'''
https://leetcode.com/problems/maximum-product-of-word-lengths
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:


Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".

Example 2:


Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".

Example 3:


Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
'''
import collections
class Solution(object):

    def maxProduct_bitm(self, words):
        numbers = []    # change to set can accelerate the speed
        for word in words:
            num = 0
            for c in word:
                num |= 1 << (ord(c) - ord('a'))
            numbers.append((len(word), num))
        
        _len, _max = len(words), 0
        for i in range(_len):
            for j in range(i+1, _len):
                if numbers[i][1] & numbers[j][1] > 0:
                    continue
                _max = max(_max, numbers[i][0] * numbers[j][0])
        return _max

s = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]; print s.maxProduct(words), s.maxProduct_bitm(words)