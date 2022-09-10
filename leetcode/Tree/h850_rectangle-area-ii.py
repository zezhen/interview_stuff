'''
https://leetcode.com/problems/rectangle-area-ii
https://leetcode.com/articles/rectangle-area-ii
We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:


Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.


Example 2:


Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.


Note:


	1 <= rectangles.length <= 200
	rectanges[i].length = 4
	0 <= rectangles[i][j] <= 10^9
	The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.

'''
from sortedcontainers import SortedDict
class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # credit to https://leetcode.com/problems/rectangle-area-ii/discuss/139835
        # It's quite complicated to caculate the overlap, need to handle many scenarios
        # It's similar as the skyline problem, which is to record the left/right boundary using 1/-1
        # we can solve this problem using similar way.

        # first record the corners with 1/-1 for each rectangle
        # we start from left most rectangle at lx, there might be one or more rectangles start from lx
        # we have (lx, ly, 1), (lx, ry, -1), so we know the y length is ry - rx, keep a count, 
        # positive means we enter a rectangle area, zero means out of rectangle, we need to process y increasingly
        # keep the total sum of y as preY

        # then move lx to right until meet the second x (preX = lx): x = lx' if overlap or x = rx if no overlap
        # no matter which one, we already have area = (x - preX) * preY
        # then x become preX for next calculation, re-calculate preY.

        mod = 10**9 + 7
        points = []
        for lx,ly,rx,ry in rectangles:
            points.append((lx, ly, 1))
            points.append((lx, ry, -1))
            points.append((rx, ly, -1))
            points.append((rx, ry, 1))
        points.sort(key=lambda (x,y,v): (x, -y))

        sd = SortedDict()  # sd = {}    # to keep the sorted y for x
        

        def calY():
            ans, prev, count = 0, None, 0
            for k, v in sd.iteritems():    # for k, v in sorted(sd.iteritems()):
                if prev != None and count > 0:
                    ans += k - prev
                count += v  # after several iteration, some v become 0, we can either remove it or just ignore it
                prev = k
            return ans

        preX = preY = None
        ans = 0
        for i, (x, y, v) in enumerate(points):
            sd[y] = sd.get(y, 0) + v
            if i == len(points) - 1 or points[i+1][0] > x:
                if preX != None:
                    ans += (x - preX) * preY % mod
                preX = x
                preY = calY()
        return ans % mod

s = Solution()
print s.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]) == 6
print s.rectangleArea([[0,0,2,2],[1,1,3,3]]) == 7
print s.rectangleArea([[0,0,3,2],[1,1,3,3]]) == 8

