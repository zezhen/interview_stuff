'''
https://leetcode.com/problems/add-binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:


Input: a = "11", b = "1"
Output: "100"

Example 2:


Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or len(a) <= 0:
            return b
        elif not b or len(b) <= 0:
            return a
        
        sum, carry = int(a, 2), int(b, 2)

        while carry > 0:
            tmps = sum
            sum = tmps ^ carry
            carry = (tmps & carry) << 1
 
        return format(sum, 'b')