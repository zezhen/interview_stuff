'''
https://leetcode.com/problems/reverse-pairs/description/

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

'''
import bisect
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        queue = []
        ans = 0
        for n in nums:
            i = bisect.bisect(queue, n * 2)
            if i < len(queue):
                ans += len(queue) - i
            bisect.insort(queue, n)
        return ans