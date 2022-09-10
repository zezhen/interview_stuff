'''
https://leetcode.com/problems/subarray-product-less-than-k
https://leetcode.com/articles/subarray-product-less-than-k
Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.



Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
'''
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        l, r, product, count = 0, 0, 1, 0
        # use two pointers, start from l, product all the numbers 
        # that less than k until r (exclusive), so for the l, there
        # are r - l subarrays meet condition.
        while True:
            while l < len(nums) and nums[l] >= k: 
                l += 1
                r = l
                product = 1
            if l >= len(nums): break
            
            while r < len(nums) and product * nums[r] < k:
                product *= nums[r]
                r += 1
            else:
                count += r - l
            
            product /= nums[l]
            l += 1
        
        return count