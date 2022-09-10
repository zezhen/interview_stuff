'''
https://leetcode.com/problems/contains-duplicate-ii
https://leetcode.com/articles/contains-duplicate-ii
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


Example 1:


Input: nums = [1,2,3,1], k = 3
Output: true



Example 2:


Input: nums = [1,0,1,1], k = 1
Output: true



Example 3:


Input: nums = [1,2,3,1,2,3], k = 2
Output: false




'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        
        dup = {}
        
        for i,x in enumerate(nums):
            if x in dup and i - dup[x] <= k:
                return True
            else:
                dup[x] = i
        
        return False
            