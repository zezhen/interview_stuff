'''
https://leetcode.com/problems/wiggle-sort
https://leetcode.com/articles/wiggle-sort

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # If i is odd, then nums[i] >= nums[i - 1]; If i is even, then nums[i] <= nums[i - 1].
        # swap i and i-1 if necessary