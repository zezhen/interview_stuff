'''
https://leetcode.com/problems/permutations-ii
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:


Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''
class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        def bt(nums,path):
            if len(nums) == 0:
                res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: continue
                bt(nums[:i]+nums[i+1:],path + [nums[i]])
        bt(nums,[])
        return res

    def permuteUnique0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count, total = 1, self.calculateTotal(nums)
        result = [nums[:]]
        while count < total:
            self.nextPermutation(nums)
            result.append(nums[:])
            count += 1
        return result
    
    def calculateTotal(self, nums):
        _dict = {}
        for n in nums:
            _dict[n] = (_dict[n] if n in _dict else 0) + 1
        total = reduce(lambda x,y:x*y, range(1, len(nums)+1))
        for k,v in _dict.iteritems():
            total /= reduce(lambda x,y:x*y, range(1, v+1))
        return total

    def nextPermutation(self, nums):
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
nums=[1,2,2,3,3,4]; print s.permuteUnique(nums) == s.permuteUnique0(nums)