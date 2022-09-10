'''
https://leetcode.com/problems/score-of-parentheses/description/

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
'''

class Solution(object):
    def scoreOfParentheses(self, S):
        stack = []

        for i, ch in enumerate(S):
            # print i, ch, stack
            if ch == '(':
                stack.append(ch)
            else:
                if stack[-1] == '(':
                    stack.pop() # pop out (
                    num = 1
                else:
                    num = stack.pop()
                    while stack and stack[-1] != '(':
                        num += stack.pop()
                    if stack and stack[-1] == '(': 
                        num *= 2
                        stack.pop()
                stack.append(num)

        return sum(stack)

    def scoreOfParentheses2(self, S):
        """
        :type S: str
        :rtype: int
        """
        cache = []
        for c in S:
        	if c == '(':
        		cache.append(c)
        	elif c == ')':
        		doDouble = False
        		if cache[-1] == '(':
        			cache.pop()
        			value = 1
        		else:
        			value = cache.pop()
        			doDouble = True

    			while len(cache) > 0 and cache[-1] != '(':
    				value += cache.pop()
    			if doDouble:
    				cache.pop()  # need to pop (
    				value *= 2
        		
        		cache.append(value)
        
        return sum(cache)

s = Solution()
assert s.scoreOfParentheses("()") == 1
assert s.scoreOfParentheses("(())") == 2
assert s.scoreOfParentheses("((())()(()))") == 10
assert s.scoreOfParentheses("()(())") == 3
assert s.scoreOfParentheses("()(()())") == 5
