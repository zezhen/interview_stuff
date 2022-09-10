'''
https://leetcode.com/problems/the-skyline-problem/description/

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

https://assets.leetcode.com/uploads/2018/10/22/skyline1.png
https://assets.leetcode.com/uploads/2018/10/22/skyline2.png


The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''

# sortedcontainers is not in standard built-in library
# http://www.grantjenks.com/docs/sortedcontainers/

from sortedcontainers import SortedList
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        # credit to https://briangordon.github.io/2014/08/the-skyline-problem.html
        # the basic idea is to record the building left/right corners, then scan from left most to right
        # if enter a building, and its height higher than cur_height, it become the new hight, otherwise omitted
        # if leave a building, cur_height ended, the next max height become new cur_height, thus we need sorted list to record the heights

        points = []
        for b in buildings:
            points.append((b[0], - b[2]))   # start
            points.append((b[1], b[2]))     # end
        points.sort()

        ans = []
        pq = SortedList() # pq = []
        
        pq.add(0) # pq.append(0)
        prev_height = 0
        for p in points:
            if p[1] < 0:
                pq.add(- p[1]) # pq.append(- p[1])
            else:
                pq.remove(p[1])
                
            cur_height = pq[-1] # cur_height = max(pq)
            if cur_height != prev_height:
                ans.append([p[0], cur_height])
                prev_height = cur_height
        return ans


# also refer to 

s = Solution()
print s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) == [[2,10], [3,15], [7,12], [12,0], [15,10], [20,8], [24,0]]
print s.getSkyline([[0,2,3],[2,5,3]]) 