'''
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.append([], 0, n)
        return self.result
    
    def append(self, queue, cap, remaining):
        if remaining == 0 and cap == 0:
            self.result.append("".join(queue))
            return
    
        
        if remaining > 0:
            queue.append('(')
            self.append(queue, cap + 1, remaining - 1)
            queue.pop()
        else:
            # append all ')' directly, no need recur
        
        if cap > 0:
            queue.append(')')
            self.append(queue, cap - 1, remaining)
            queue.pop()
        