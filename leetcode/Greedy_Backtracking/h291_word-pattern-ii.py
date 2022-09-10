'''
https://leetcode.com/problems/word-pattern-ii

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
Notes:
You may assume both pattern and str contains only lowercase letters.

'''
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern: return str == ''
        if not str: return pattern == ''
        
        # check repeat
        i = (pattern + pattern)[1:-1].find(pattern)
        if i != -1: # there is repeated substring
            subpattern = pattern[:i+1]
            times = len(pattern) / len(subpattern)
            if len(str) % times != 0: return False
            substr = str[:len(str)/times]
            if substr * times != str: return False
            pattern, str = subpattern, substr

        # backtracking check pattern vs str
        def dfs(pattern, str, dict):
            if len(pattern) == 0 and len(str) > 0: return False
            if len(pattern) == len(str) == 0: return True
            for end in range(1, len(str)-len(pattern)+2): # len(s) - end >= len(pattern) - 1
                # print end, len(str), len(pattern)
                if pattern[0] not in dict and str[:end] not in dict.values():
                    dict[pattern[0]] = str[:end]
                    if dfs(pattern[1:], str[end:], dict): return True
                    del dict[pattern[0]]
                elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
                    if dfs(pattern[1:], str[end:], dict): return True
            return False

        return dfs(pattern, str, {})


s = Solution()
print s.wordPatternMatch('', '')
print s.wordPatternMatch('abab', 'redblueredblue')

