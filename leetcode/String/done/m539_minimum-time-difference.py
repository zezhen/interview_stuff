'''
https://leetcode.com/problems/minimum-time-difference/description/

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.

'''

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

'''
Hour:Minutes guarantee hh:MM format
sort time points list
min(a[i+1]-a[i]) for all i in [0, n) or a[0]-a[n-1]
'''