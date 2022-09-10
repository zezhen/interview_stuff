'''
https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
'''

import bisect, collections
class Solution(object):
    # wrong solution, thought I cound simply patch the LIS solution
    def findNumberOfLIS_fail(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        queue = []
        count = 0
        for n in nums:
            i = bisect.bisect_left(queue, n)
            if i >= len(queue):
                queue.append(n)
                # new LIS, original count is still valid
                if i == 0: count = 1
            else:
                queue[i] = n
                # add another LIS, count inc 1
                if i == len(queue) - 1: count += 1
        return count

    def findNumberOfLIS(self, nums):
        lg = [0] * len(nums)
        ct = [0] * len(nums)
        maxct, maxlg = 0, 0
        for i in xrange(len(nums)):
            lg[i] = ct[i] = 1
            for j in xrange(i):
                if nums[i] > nums[j]:
                    if lg[i] == lg[j] + 1: ct[i] += ct[j]
                    if lg[i] < lg[j] + 1:
                        lg[i] = lg[j] + 1
                        ct[i] = ct[j]

            if lg[i] == maxlg: maxct += ct[i]
            if lg[i] > maxlg:
                maxlg = lg[i]
                maxct = ct[i]
        return maxct

s = Solution()
assert s.findNumberOfLIS([]) == 0
assert s.findNumberOfLIS([1]) == 1
assert s.findNumberOfLIS([1,2,3,4,5]) == 1
assert s.findNumberOfLIS([5,4,3,2,1]) == 5
assert s.findNumberOfLIS([2,2,2,2,2]) == 5
assert s.findNumberOfLIS([1,3,5,4,7]) == 2
assert s.findNumberOfLIS([1,3,5,4,7,5]) == 3
assert s.findNumberOfLIS([1,3,5,4,7,5,1,2,3]) == 3
assert s.findNumberOfLIS([3,1,2]) == 1