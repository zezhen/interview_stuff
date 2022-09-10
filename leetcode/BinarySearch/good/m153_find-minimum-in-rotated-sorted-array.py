'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary(nums, start, end):
            if start == end:
                return nums[start] if start == len(nums)-1 else nums[0]
            mid = start + (end-start)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[0] > nums[mid]:
                return binary(nums, start, mid)
            else:
                return binary(nums, mid+1, end)
        return binary(nums, 0, len(nums))