'''
https://leetcode.com/problems/next-greater-element-iii/description/

# similar to 
# e496: https://leetcode.com/problems/next-greater-element-i/description/
# m503: https://leetcode.com/problems/next-greater-element-ii/description/


Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
'''

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
'''
variant to permutation problem
first find all digits given n
scan from low-order, find first i that d[i] < d[i+1], if there is not i, return -1
scan from low-order, find first j that d[j] > d[i], swap i and  j
'''


