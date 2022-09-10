'''
https://leetcode.com/problems/continuous-subarray-sum/description/

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) <= 1: return False
        if k == 1 or sum(nums) == 0: return True
        if k == 0: return False

        # if there is such subarray exist, sum(nums[i:j]) % k = 0, sum(nums[:j]) % k == sum(nums[i-1]) % k
        pos = {0:-1}
        i, _len, _sum = 0, len(nums), 0
        while i < _len:
            _sum = (_sum + nums[i]) % k
            if _sum in pos:
                if pos[_sum] < i - 1:   # make sure there are at least two elements
                    # print nums[pos[_sum]+1:i+1], sum(nums[pos[_sum]+1:i+1])
                    return True
            else:
                pos[_sum] = i
            i += 1
        
        return False