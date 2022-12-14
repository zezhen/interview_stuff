'''
https://leetcode.com/problems/factorial-trailing-zeroes
Given an integer n, return the number of trailing zeroes in n!.

Example 1:


Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:


Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
'''
import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        factor = 5
        count = 0
        while n >= factor:
            count += n / factor
            factor *= 5
        return count