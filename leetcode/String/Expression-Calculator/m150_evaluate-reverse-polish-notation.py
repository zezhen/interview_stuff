'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = set(['+','-','*','/'])

        number_last_index = 0
        for i, token in enumerate(tokens):
        	if token not in operators:
        		tokens[number_last_index] = int(token)
        		number_last_index += 1
        		continue

        	# token is operation, evaluate it
        	if token == '+':
        		res = tokens[number_last_index-2] + tokens[number_last_index-1]
        	elif token == '-':
        		res = tokens[number_last_index-2] - tokens[number_last_index-1]
        	elif token == '*':
        		res = tokens[number_last_index-2] * tokens[number_last_index-1]
        	else:
        		res = tokens[number_last_index-2] / tokens[number_last_index-1]
        		# python integer division by negative number will floor to negative infinity
        		if res < 0:
        			res = - (abs(tokens[number_last_index-2]) / abs(tokens[number_last_index-1]))

        	# put result at the position of first number
        	number_last_index -= 1
        	tokens[number_last_index - 1] = res
        return tokens[0]

s = Solution()
assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22