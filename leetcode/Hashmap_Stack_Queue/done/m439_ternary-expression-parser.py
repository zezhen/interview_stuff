'''
https://leetcode.com/problems/ternary-expression-parser

Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).

Note:

The length of the given string is <= 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.
Example 1:

Input: "T?2:3"

Output: "2"

Explanation: If true, then result is 2; otherwise result is 3.
Example 2:

Input: "F?1:T?4:5"

Output: "4"

Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"
Example 3:

Input: "T?T?F:5:3"

Output: "F"

Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"
'''
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
        def parse(start):
          i = start
          if expression[i] in ['T', 'F'] and i+1 < len(expression) and expression[i+1] == '?':
              j, resT = parse(i+2)
              assert expression[j] == ':'
              j, resF = parse(j+1)
              return j, resT if expression[i] == 'T' else resF
          else:
              while i < len(expression) and expression[i] not in ['?',':']:
                  i += 1
              return i, expression[start:i]

        return parse(0)[1]


s = Solution()

print s.parseTernary("T") == 'T'
print s.parseTernary("3") == '3'
print s.parseTernary("T?3:4") == '3'
print s.parseTernary("T?3:T?1:2") == '3'
print s.parseTernary("F?3:T?1:2") == '1'
print s.parseTernary("F?T?3:4:T?1:2") == '1'
print s.parseTernary("T?T?F:5:3") == 'F'
print s.parseTernary("T?F?F:T:F") == 'T'
