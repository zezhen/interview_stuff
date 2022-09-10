'''
https://leetcode.com/problems/bitwise-and-of-numbers-range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:


Input: [5,7]
Output: 4


Example 2:


Input: [0,1]
Output: 0'''

import math
class Solution(object):
    def rangeBitwiseAnd_fastest(self, m, n):
        length = (m ^ n).bit_length() 
        n >>= length
        return n << length

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        
        s = int(math.log(m, 2))
        e = int(math.log(n, 2))
        
        if s != e:
            return 0
        else:
            ret = m
            for i in range(m+1, n+1):
                ret &= i
            return ret