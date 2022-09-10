'''
https://leetcode.com/problems/count-numbers-with-unique-digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.


Example:


Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 <= x < 100, 
             excluding 11,22,33,44,55,66,77,88,99

'''

import operator

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1
        
        count, base = 10, 1
        for i in range(1, n):
            base *= (10 - i)
            count += 9 * base
        
        return count