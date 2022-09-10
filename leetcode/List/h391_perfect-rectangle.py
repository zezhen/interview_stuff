'''
https://leetcode.com/problems/perfect-rectangle/description/

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
https://assets.leetcode.com/uploads/2018/10/22/rectangle_perfect.gif
Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
https://assets.leetcode.com/uploads/2018/10/22/rectangle_separated.gif
Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]
https://assets.leetcode.com/uploads/2018/10/22/rectangle_hole.gif
Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]
https://assets.leetcode.com/uploads/2018/10/22/rectangle_intersect.gif
Return false. Because two of the rectangles overlap with each other.

'''

class Solution(object):
    def isRectangleCover_fastest(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        area,corners = 0,set()
        a,c = lambda: (X-x)*(Y-y),lambda: {(x,y),(x,Y),(X,y),(X,Y)}
        for x,y,X,Y in rectangles: 
            print corners
            area += a()
            corners ^= c()
        
        x,y,X,Y = (f(z) for f,z in zip((min,min,max,max),zip(*rectangles)))
        print x,y,X,Y
        print area, a(), corners, c()
        return area==a() and corners==c()

    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        import sys
        # keep most left top and right botton points
        # check whether area is the sum area of all rectangles
        left,bottom,right,top = sys.maxint, sys.maxint, -sys.maxint,-sys.maxint
        area = 0
        points = set()
        for x1,y1,x2,y2 in rectangles:
            left = min(x1, left)
            bottom = min(y1, bottom)
            right = max(x2, right)
            top = max(y2, top)
            area += (y2-y1) * (x2-x1)
            points.add((x1,y1))
            points.add((x2,y2))
            points.add((x1,y2))
            points.add((x2,y1))
        
        if area != (top - bottom) * (right - left):
            return False
        
        for x,y in [(left,bottom), (left,top), (right,bottom),(right,top)]:
            if (x,y) not in points: return False
        
        # check area is even distributed
        height = [0] * (right-left)
        width = [0] * (top - bottom)
        for x1,y1,x2,y2 in rectangles:
            for i in xrange(x1,x2):
                height[i-left] += y2-y1
            for i in xrange(y1,y2):
                width[i-bottom] += x2-x1
        
        return len(set(height)) == 1 and len(set(width)) == 1

s = Solution()
print s.isRectangleCover_fastest([[0,0,1,1],[0,0,1,1],[1,1,2,2],[1,1,2,2]])