'''
https://leetcode.com/problems/valid-parenthesis-string/description/

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''



class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
        at beginning, I want to keep count for nP and nS, 
        nP ++ when meet '(', -- when meet ')', nS ++ when meet '*'
        if meet ')' and nS > 0, nS --, otherwise False
        this cannot keep the order of * with ( or ), e.g. "*((()))("

        for *, we have three choices: empty, ( or ), one solution is dfs to check all possibilities.
        or we can keep two counters to specifiy the min/max pairs we need to process, e.g. "(**())"

        i = 0: one pair
        i = 1: 2 pairs if * => (, 1 pair if * is empty, or 0 pair if * => )
        i = 2: 3 pairs if both * => (, 2 pair if one * is empty and another is (, 0 if one * is empty and another is )
        ...

        so we can keep counting the min/max pairs by now, if max count is negative, means there is one ) more, return False
        otherwise we need to check whether we need to process min count, string is valid if min is 0, otherwise return False
        '''

        low = high = 0
        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                if low > 0: low -= 1
                high -= 1
            else:
                if low > 0: low -= 1
                high += 1

            if high < 0:
                return False
        return low == 0

s = Solution()
print s.checkValidString("(") == False
print s.checkValidString(")") == False
print s.checkValidString("*") == True
print s.checkValidString("()")
print s.checkValidString("(*)")
print s.checkValidString("(*))")
print s.checkValidString("((*)")
print s.checkValidString("(((*)") == False
print s.checkValidString("(*)))") == False
print s.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*") == False
print s.checkValidString("*((()))(") == False

