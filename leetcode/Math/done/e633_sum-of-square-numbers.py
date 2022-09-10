'''
https://leetcode.com/problems/sum-of-square-numbers
https://leetcode.com/articles/sum-of-square-numbers

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.


Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5




Example 2:

Input: 3
Output: False


'''
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        # sqrt(c) size array a, a[i] = (i+1)^2
        # problem become 2-sum