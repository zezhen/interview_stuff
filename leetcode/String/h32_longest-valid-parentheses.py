'''

https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # DP problem, use count[i] keep the max count ending by index i
        # if s[i] = (, count[i] = 0
        # if s[i] = ), s[i-1] = (, it's a pair, count[i] = count[i-2] + 2
        #              s[i-1] = ) and s[i-1-count[i-1]] = (,  count[i] = count[i-1] + 2 + count[i-2-count[i-1]]

        count = [0] * len(s)
        ans = 0
        for i in xrange(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    count[i] = (count[i-2] if i >= 2 else 0) + 2
                elif i-1-count[i-1] >= 0 and s[i-1-count[i-1]] == '(':
                    count[i] = count[i-1] + 2
                    if i-2-count[i-1] >= 0:
                        count[i] += count[i-2-count[i-1]]
                ans = max(ans, count[i])
        return ans

s = Solution()
print s.longestValidParentheses("(()") == 2
print s.longestValidParentheses(")()())") == 4
print s.longestValidParentheses("()()(())") == 8
print s.longestValidParentheses("()()((())") == 4
print s.longestValidParentheses("(()())") == 6


