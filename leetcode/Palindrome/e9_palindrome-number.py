'''
https://leetcode.com/problems/palindrome-number
https://leetcode.com/articles/palindrome-number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:


Input: 121
Output: true


Example 2:


Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:


Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Follow up:

Coud you solve it without converting the integer to a string?
'''
import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        print x
        if x < 0:
            return False
        if 0 <= x <= 9:
            return True
        
        y = x
        high = 1
        while y > 0:
            y /= 10
            high *= 10
        
        y = x
        high /= 10
        low = 10
        while high > 0:
            t1 = y / high
            t2 = y % low
            
            if t1 != t2:
                return False
            
            y = (y - t1 * high) / 10
            high /= 100
        
        return True

        
        
        