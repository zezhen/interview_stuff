'''
https://leetcode.com/problems/different-ways-to-add-parentheses/description/

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''

import re
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        if not input:
            return []

        values = re.split('[+\-\*]', input)
        ops, _len = [], 0
        for v in values[:-1]:
            ops.append(input[_len + len(v)])
            _len += len(v) + 1
        values = map(int, values)

        return self.calculateAsTree(0, len(ops) - 1, ops, values)
        
    
    def calculateAsTree(self, s, e, ops, values):
        if s > e:
            return [values[s]]

        if s == e:
            return self.mutipleOp(ops[s], [values[s]], [values[s+1]])

        result = []
        i = s
        while i <= e:
            lefts = self.calculateAsTree(s, i-1, ops, values) 
            rights = self.calculateAsTree(i+1, e, ops, values)
            result.extend(self.mutipleOp(ops[i], lefts, rights))
            i += 1

        return result

    def mutipleOp(self, op, lefts, rights):
        result = []
        for left in lefts:
            for right in rights:
                if op == '+':
                    result.append(left + right)
                elif op == '-':
                    result.append(left - right)
                elif op == '*':
                    result.append(left * right)
        return result