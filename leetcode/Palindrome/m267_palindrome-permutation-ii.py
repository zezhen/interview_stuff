'''
https://leetcode.com/problems/palindrome-permutation-ii
https://leetcode.com/articles/palindrome-permutation-ii

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
'''
from collections import Counter
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = Counter(s)

        elements = counter.most_common()
        odd = 0
        for c,n in reversed(elements):
            if n % 2 == 1:
                odd += 1
                if odd == 2: return []

        # refer to others's solution, we can construct a candidate list
        # that contain half chars, e.g. aabb, the candidate are ['a', 'b']
        # for odd cases, use a string mid to keep it.
        ans = []
        def dfs(st, _len):
            if len(st) == _len:
                ans.append(st)
                return

            for c, n in elements:



