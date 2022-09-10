'''
https://leetcode.com/problems/count-of-range-sum/description/

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

'''

import bisect
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums or lower > upper: return 0

        # for nums[i], suppose exists index j that make lower <= S(i, j) <= upper
        # then we can get lower <= S(0, j) - S(0, i-1) <= upper, we can pre-compute S(0, k)
        # S(0, j) - upper <= S(0, i-1) <= S(0, j) - lower, 
        # so we need to maintain an ordered struct and binary search for the range
        
        acc = {-1:0}
        for i in xrange(len(nums)):
            acc[i] = acc[i-1] + nums[i]

        queue = [0] # left boundary
        ans = 0
        for i in xrange(len(nums)):
            l = bisect.bisect_left(queue, acc[i] - upper)
            # print acc[i] - upper, queue, l
            if l < len(queue):
                r = bisect.bisect(queue, acc[i] - lower)
                ans += (r - l)
            bisect.insort(queue, acc[i])    # O(n), need to switch to SortedList

        return ans

s = Solution()
print s.countRangeSum([1,2,-3], 2, -2) == 0
print s.countRangeSum([], -2, 2) == 0
print s.countRangeSum([3], -2, 2) == 0
print s.countRangeSum([1], -2, 2) == 1
print s.countRangeSum([-2,5,-1], -2, 2) == 3
print s.countRangeSum([-2,-2,-2,4,4,0], -2, 2) == 9
print s.countRangeSum([-2,5,-1,-2,-2], -2, -2) == 4