'''
https://leetcode.com/problems/reverse-integer
https://leetcode.com/articles/reverse-integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:


Input: 123
Output: 321


Example 2:


Input: -123
Output: -321


Example 3:


Input: 120
Output: 21


Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution(object):
    def reverse(self, x): 
        neg, x = x < 0, abs(x)
        ans = 0
        while x > 0:
            temp = ans * 10 + x % 10
            if temp / 10 != ans:
                return 0
            ans = temp
            x /= 10
        return - ans if neg else ans