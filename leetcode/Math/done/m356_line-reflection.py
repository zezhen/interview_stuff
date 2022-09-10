'''
https://leetcode.com/problems/line-reflection

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:

Input: [[1,1],[-1,1]]
Output: true
Example 2:

Input: [[1,1],[-1,-1]]
Output: false
Follow up:
Could you do better than O(n^2) ?
'''

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        # hashmap