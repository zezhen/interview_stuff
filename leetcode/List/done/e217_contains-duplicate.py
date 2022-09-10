'''
https://leetcode.com/problems/contains-duplicate
https://leetcode.com/articles/contains-duplicate
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:


Input: [1,2,3,1]
Output: true

Example 2:


Input: [1,2,3,4]
Output: false

Example 3:


Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _set = set()
        _set.update(nums)
        return len(_set) != len(nums)
        