'''
https://leetcode.com/problems/fraction-to-recurring-decimal
https://leetcode.com/articles/fraction-to-recurring-decimal
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:


Input: numerator = 1, denominator = 2
Output: "0.5"


Example 2:


Input: numerator = 2, denominator = 1
Output: "2"

Example 3:


Input: numerator = 2, denominator = 3
Output: "0.(6)"

'''
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # process zero scenario
        if denominator == 0: return 'NAN'
        if numerator == 0: return "0"
        
        # process negative scenario
        sign = 1
        if numerator < 0: 
            sign *= -1
            numerator = -1 * numerator
        if denominator < 0: 
            sign *= -1
            denominator = -1 * denominator
        
        # process the integer part
        ans = []
        if sign == -1: ans.append('-')
        ans.append(numerator / denominator)
        ans.append('.')
        numerator = numerator % denominator
        
        # fractional part, 
        # we use array fraction to keep all divisors
        # use memo to keep the residual of mode and the index in fraction array
        # once we meet the residual exist in memo again, it means repeated 
        # insert '(' to the right place.
        index, memo, fraction = 0, {}, [] 
        while numerator > 0:
            numerator *= 10
            
            if numerator in memo:
                start = memo[numerator]
                fraction.insert(start, '(')
                fraction.append(')')
                break
            
            divisor = numerator / denominator
            fraction.append(divisor)
            memo[numerator] = index
            index += 1
            
            numerator %= denominator
            

        
        if len(fraction) <= 0:
            ans.pop()
        else:
            ans.extend(fraction)
            
        return ''.join(map(str,ans))
            