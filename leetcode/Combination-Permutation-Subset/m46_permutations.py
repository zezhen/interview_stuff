'''
https://leetcode.com/problems/permutations
Given a collection of distinct integers, return all possible permutations.

Example:


Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''
class Solution(object):
    def permute(self, nums):
        ans = []
        count, total = 0, reduce(lambda x,y:x*y, range(1, len(nums)+1))
        while count < total:
            for i in xrange(len(nums)-1):
                j = i + 1
                nums[i], nums[j] = nums[j], nums[i]
                print nums
                ans.append(nums[:])
            count += len(nums) - 1
        return ans


    def permute1(self, nums):
        res = []
        def bt(nums,path):
            if len(nums) == 0:
                res.append(path)
            for i in range(len(nums)):
                bt(nums[:i]+nums[i+1:],path + [nums[i]])
        bt(nums,[])
        return res

    def permute0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count, total = 1, reduce(lambda x,y:x*y, range(1, len(nums)+1))
        result = [nums[:]]
        while count < total:
            self.nextPermutation(nums)
            result.append(nums[:])
            count += 1
        return result

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
nums = [1,2,3,4]
p = s.permute(nums)
p0 = s.permute0(nums)
p1 = s.permute1(nums)

print sorted(p)
print sorted(p0) == sorted(p1)