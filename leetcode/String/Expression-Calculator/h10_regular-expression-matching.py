'''
https://leetcode.com/problems/regular-expression-matching/description/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        MAX = len(p)
        # compile pattern string
        i, rules = 0, []
        min_len = 0
        while i < len(p):
            c = p[i]
            if i + 1 < len(p) and p[i+1] == '*':
                if not rules or rules[-1] != (c, 0):
                    rules.append((c, 0))
                i += 1
            else:
                rules.append((c, 1))
                min_len += 1
            i += 1

        if len(s) < min_len: return False

        i, j, stack = 0, 0, []
        while min_len > 0 or j < len(s):
            
            if i < len(rules) and j < len(s) and (rules[i][0] == '.' or rules[i][0] == s[j]): 
                if rules[i][1] == 1:
                    i += 1
                    min_len -= 1
                else:
                    # cp can match arbitrary times,
                    # backup the scenario that if cp stop match here
                    if i < len(rules) - 1: 
                        stack.append((i+1, j, min_len))  # don't have to match now
                        stack.append((i+1, j+1, min_len)) # match then move forward
                j += 1
            elif i < len(rules) and rules[i][1] == 0:
                i += 1
            elif len(stack) > 0:
                # restore another scenario
                i, j, min_len = stack.pop()
            else:
                return False
            
        return True

    def isMatch_dfs(self, s, p):
        if not p: return not s
        if len(p) == 1:
            if len(s) != 1: return False
            return s == p

        if s and (p[0] == '.' or p[0] == s[0]):
            if p[1] == '*':
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            elif p[1] == '+':
                return self.isMatch(s[1:], p[2:])
            else:
                return self.isMatch(s[1:], p[1:])
        return p[1] == '*' and self.isMatch(s, p[2:])


s = Solution()

assert s.isMatch("aa", "aa") == True
assert s.isMatch("aa", "a") == False
assert s.isMatch("aaaaa", "a*") == True
assert s.isMatch("ab", ".*") == True
assert s.isMatch("aab", "c*a*b") == True
assert s.isMatch("abc", "a*b.*") == True
assert s.isMatch("mississippi", "mis*is*p*.") == False
assert s.isMatch("b", ".*b") == True
assert s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False



