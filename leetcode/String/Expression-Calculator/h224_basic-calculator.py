'''
https://leetcode.com/problems/basic-calculator/description/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

'''
from collections import deque
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        stack = deque()
        ans = 0
        num, sign = 0, 1

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+' or ch == '-':
                ans += num * sign
                num = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                stack.append(ans)
                stack.append(sign)
                # reset all parameters
                num, sign = 0, 1
                ans = 0
            elif ch == ')':
                ans += sign * num
                ans *= stack.pop()  # pop out the sign before parenthesis
                ans += stack.pop()  # pop out the number before parenthesis
                num, sign = 0, 1

        if num > 0:
            ans += sign * num
        return ans


s = Solution()
print s.calculate('1 + 1') == 2
print s.calculate(' 2-1 + 2 ') == 3
print s.calculate('(1+(4+5+2)-3)+(6+8)') == 23


