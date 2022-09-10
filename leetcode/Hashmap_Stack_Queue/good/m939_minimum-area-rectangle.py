'''
https://leetcode.com/problems/minimum-area-rectangle
https://leetcode.com/articles/minimum-area-rectangle
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 


Example 1:


Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4



Example 2:


Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


 

Note:


	1 <= points.length <= 500
	0 <= points[i][0] <= 40000
	0 <= points[i][1] <= 40000
	All points are distinct.


'''
import collections, sys
class Solution(object):
    def minAreaRect(self, points):
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x       # cache it, wait other x to check, smart!
        return res if res < float('inf') else 0


    def minAreaRect_On2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        pointSet = set(map(tuple, points))
        minArea = sys.maxint
        for i in xrange(len(points)):
            for j in xrange(i+1, len(points)):

                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 != x2 and y1 != y2 and (x1, y2) in pointSet and (x2, y1) in pointSet:
                    minArea = min(minArea, abs(x1-x2)*abs(y1-y2))
                    
        return minArea if minArea < sys.maxint else 0

s = Solution()
print s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]) == 4
print s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]) == 2

