'''
https://leetcode.com/problems/out-of-boundary-paths/description/

There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

https://assets.leetcode.com/uploads/2018/10/13/out_of_boundary_paths_1.png

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

https://assets.leetcode.com/uploads/2018/10/12/out_of_boundary_paths_2.png

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].

'''

class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
    	memo = {}
    	modole = 10**9 + 7
    	def count(x, y, c):
    		if (x, y, c) in memo: return memo[(x, y, c)]
    		
    		if x<0 or x >= m: return 1
    		if y<0 or y >= n: return 1
    		if c <= 0: return 0

    		acc = count(x-1, y, c-1) + count(x+1, y, c-1) + count(x, y-1, c-1) + count(x, y+1, c-1)
    		acc = acc % modole
    		memo[x, y, c] = acc
    		return acc

    	return count(i, j, N)


s = Solution()
assert s.findPaths(m = 2, n = 2, N = 0, i = 0, j = 0) == 0
assert s.findPaths(m = 1, n = 1, N = 1, i = 0, j = 0) == 4
assert s.findPaths(m = 2, n = 2, N = 2, i = 0, j = 0) == 6
assert s.findPaths(m = 1, n = 3, N = 3, i = 0, j = 1) == 12
assert s.findPaths(m = 50, n = 50, N = 50, i = 25, j = 25) == 276775132