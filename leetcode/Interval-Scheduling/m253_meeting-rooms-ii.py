'''
https://leetcode.com/problems/meeting-rooms-ii
https://leetcode.com/articles/meeting-rooms-ii

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # refer to https://leetcode.com/problems/meeting-rooms-ii/discuss/67855
        starts = sorted(map(lambda t:t[0], intervals))
        ends = sorted(map(lambda t:t[1], intervals))

        rooms, endIndex = 0,0
        for s in starts:
            if s < ends[endIndex]:
                rooms += 1
            else:
                endIndex += 1
        return rooms

s = Solution()
print s.minMeetingRooms([[0, 30],[5, 10],[15, 20]])
print s.minMeetingRooms([[7,10],[2,4]])