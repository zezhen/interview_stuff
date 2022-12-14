'''
https://leetcode.com/problems/power-of-two
Given an integer, write a function to determine if it is a power of two.

Example 1:


Input: 1
Output: true 
Explanation: 20 = 1


Example 2:


Input: 16
Output: true
Explanation: 24 = 16

Example 3:


Input: 218
Output: false
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        counter = 0
        while n >= 1 and counter < 1:
            counter += n & 1
            n >>= 1
        return n == 0 and counter == 1