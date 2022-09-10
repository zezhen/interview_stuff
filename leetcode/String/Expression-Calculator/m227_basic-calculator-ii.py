'''
https://leetcode.com/problems/basic-calculator-ii/description/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
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
        num, sign = 0, '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(- num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(stack.pop() // num)
                sign = ch
                num = 0

        if num > 0:
            stack.append(num)

        return sum(stack)

s = Solution()
print s.calculate('3+2*2') == 7
print s.calculate('3/2') == 1
print s.calculate('3+5 / 2') == 5