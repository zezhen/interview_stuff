'''
https://leetcode.com/problems/next-permutation
https://leetcode.com/articles/next-permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
'''
class Solution(object):

    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)
        for j in range(i,n):
            if nums[j] > nums[i-1]:
                self.swap(nums,i-1,j)
                break
    
    def reverse(self,nums,i,j):
        for k in range(i,(i+j)/2+1):
            self.swap(nums,k,i+j-k)
    def swap(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i]

    def nextPermutation2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        r = len(nums) - 1
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            nums.sort()
            return
        
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = sorted(nums[i+1:])

s = Solution()

from random import shuffle

for i in xrange(100):
    nums = range(100)
    shuffle(nums)
    assert s.nextPermutation2(nums) == s.nextPermutation(nums)