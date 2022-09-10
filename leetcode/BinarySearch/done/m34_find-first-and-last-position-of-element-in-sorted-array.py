'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.bidirection_binary_search(nums, target)
        end = self.bidirection_binary_search(nums, target, False)
        return [start, end]
    
    def bidirection_binary_search(self, nums, target, left=True):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) / 2
            if target < nums[m] or left and target == nums[m]:
                r = m - 1
            elif target > nums[m] or not left and target == nums[m]:
                l = m + 1
                
        index = l if left else r
                
        return index if 0 <= index < len(nums) and nums[index] == target else -1
                
        