'''
https://leetcode.com/problems/house-robber-ii/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        
        if _len <= 0:
            return 0
        elif _len == 1:
            return nums[0]
        elif _len == 2:
            return max(nums[0], nums[1])
        
        return max(nums[0] + self._rob(nums, 2, _len-2), self._rob(nums, 1, _len-1))
    
    def _rob(self, nums, s, e):
        _len = e - s + 1
        
        if _len <= 0:
            return 0
        elif _len == 1:
            return nums[s]
        elif _len == 2:
            return max(nums[s], nums[s+1])
            
        money = [0] * len(nums)
        
        money[s] = nums[s]
        money[s+1] = max(nums[s], nums[s+1])
        money[s+2] = max(nums[s] + nums[s+2], nums[s+1])
        
        i = 3
        while s+i <= e:
            money[s+i] = max(money[s+i-1], money[s+i-2] + nums[s+i])
            i += 1

        return money[s+i-1]