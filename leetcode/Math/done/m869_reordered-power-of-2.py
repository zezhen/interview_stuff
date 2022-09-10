'''
https://leetcode.com/problems/reordered-power-of-2
https://leetcode.com/articles/reordered-power-of-2
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

 





Example 1:


Input: 1
Output: true



Example 2:


Input: 10
Output: false



Example 3:


Input: 16
Output: true



Example 4:


Input: 24
Output: false



Example 5:


Input: 46
Output: true


 

Note:


	1 <= N <= 10^9






'''
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        
        # N <= 10^9 < to 2^30
        # we can pre-build 30 numbers with digits counts
        # compare with N