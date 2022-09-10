'''
https://leetcode.com/problems/maximum-product-of-three-numbers
https://leetcode.com/articles/maximmum-product-of-three-numbers
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6



Example 2:

Input: [1,2,3,4]
Output: 24



Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

'''
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 3: return nums[0]*nums[1]*nums[2]
        
        p1, p2, p3 = -1, -1, -1
        n1, n2 = 0, 0
        
        for n in nums:
            x = n
            if x > p1:
                x, p1 = p1, x
            if x > p2:
                x, p2 = p2, x
            if x > p3:
                x, p3 = p3, x
            
            x = n
            if x < n1:
                x, n1 = n1, x
            if x < n2:
                x, n2 = n2, x
        
        return max(p1*p2*p3, p1*n1*n2)