'''
https://leetcode.com/problems/rectangle-area
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.



Example:


Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

Note:

Assume that the total area is never beyond the maximum possible value of int.
'''
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        lx = max(A, E)
        ly = max(B, F)
        rx = min(C, G)
        ry = min(D, H)
        
        if lx >= rx or ly >= ry:
            return 0
        
        return (rx - lx) * (ry - ly)