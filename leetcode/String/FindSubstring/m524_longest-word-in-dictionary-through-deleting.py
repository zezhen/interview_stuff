'''
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''


import collections
class Solution(object):
    def findLongestWord(self, word, wordList):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        cache = collections.defaultdict(int)
        for c in word:
            cache[c] += 1

        # O(n) time and space
        count = collections.defaultdict(int)
        ans = ""
        for w in wordList:
            count.clear()
            for c in w:
                count[c] += 1
                if count[c] > cache[c]: break
            else:
                if len(w) > len(ans) or len(w) == len(ans) and w < ans:
                    ans = w
        return ans

s = Solution()

assert s.findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) == "apple"
assert s.findLongestWord("abpcplea", ["b","c","a"]) == "a"
assert s.findLongestWord("abpcplea", ["m"]) == ""
assert s.findLongestWord("", ["m"]) == ""
assert s.findLongestWord("a", ["a"]) == "a"
assert s.findLongestWord("a", ["aaa"]) == ""
assert s.findLongestWord("aaaa", ["a"]) == "a"

