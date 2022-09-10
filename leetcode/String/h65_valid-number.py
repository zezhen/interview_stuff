'''
https://leetcode.com/problems/valid-number/description/

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        can_have_sign = can_have_point = can_have_space = can_have_exp = True
        has_digit = False    # exp should happen after digit
        
        digits = map(str, range(10))
        valid_chars = ['e', '+', '-', '.', ' ']
        valid_chars.extend(digits)
        
        for c in s:
            if c not in valid_chars: return False
            
            if c == ' ' and not can_have_space or \
                (c == '+' or c == '-') and not can_have_sign or \
                c == 'e' and (not can_have_exp or not has_digit) or \
                c == '.' and not can_have_point:
                return False
            
            if (c == '+' or c == '-'):
                can_have_space = False
                can_have_sign = False
            if c == '.':
                can_have_point = False
                can_have_sign = False
                can_have_space = False
            if c == 'e': 
                can_have_point = False
                can_have_exp = False
                can_have_sign = False
            
            if c in digits:
                can_have_sign = False
                can_have_space = False
                has_digit = True
            
        return True
            
            
            
            

import random

# print [random.randint(0, 10**9) for _ in range(10000)]
# print [random.randint(0, 999) for _ in range(100)]

s = Solution()
assert s.isNumber("12") == True
assert s.isNumber("12.") == True
assert s.isNumber(".12") == True
assert s.isNumber("12.e10") == True
assert s.isNumber("12.e") == False
assert s.isNumber("   .12e1") == True
assert s.isNumber("   +.12e1") == True
assert s.isNumber("-.12e1") == True
assert s.isNumber("+ .12e1") == False
assert s.isNumber("e12") == False
