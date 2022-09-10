'''
https://leetcode.com/problems/triangle/description/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        path_sum = []
        
        for r, arr in enumerate(triangle):
            prev = path_sum[:] # don't copy!!! just append and look back
            for c,num in enumerate(arr):
                if r == 0:
                    path_sum.append(num)
                else:
                    x = min(prev[c-1] if c > 0 else sys.maxint, prev[c] if c < len(prev) else sys.maxint) + num
                    if len(path_sum) > c:
                        path_sum[c] = x
                    else:
                        path_sum.append(x)
        return min(path_sum) if len(path_sum) > 0 else 0