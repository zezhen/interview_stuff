'''
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid
https://leetcode.com/articles/minimum-add-to-make-parentheses-valid
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:


	It is the empty string, or
	It can be written as AB (A concatenated with B), where A and B are valid strings, or
	It can be written as (A), where A is a valid string.


Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:


Input: "())"
Output: 1



Example 2:


Input: "((("
Output: 3



Example 3:


Input: "()"
Output: 0



Example 4:


Input: "()))(("
Output: 4

Note:
	S.length <= 1000
	S only consists of '(' and ')' characters.
'''

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        left = right = 0
        ans = 0
        for s in S:
            if s == '(':
                left += 1
            else:
                right += 1

            if right > left:
                ans += 1
                right = left

        if left > right:
            ans += left - right

        return ans

s = Solution()
print s.minAddToMakeValid('') == 0
print s.minAddToMakeValid('()') == 0
print s.minAddToMakeValid('(') == 1
print s.minAddToMakeValid(')') == 1
print s.minAddToMakeValid('(((') == 3
print s.minAddToMakeValid(')))') == 3
print s.minAddToMakeValid('()(())((') == 2
print s.minAddToMakeValid('()))((') == 4