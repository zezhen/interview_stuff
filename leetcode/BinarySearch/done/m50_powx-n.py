'''
https://leetcode.com/problems/powx-n/description/

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # assume n is integer
        if x == 0:
            return 0
        if n == 0:
            return 1.0
            
        if n > 0:
            return self.power(x, n)
        else:
            return 1.0 / self.power(x, -n)
        
    def power(self, x, n):
        if n == 1:
            return x
        
        v = self.power(x, n / 2)
        
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x