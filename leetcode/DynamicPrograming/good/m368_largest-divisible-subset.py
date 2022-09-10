'''
https://leetcode.com/problems/largest-divisible-subset/description/

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
'''

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

'''
the solution before is correct, but there is no need to keep all numbers in candidates.

what we need is to keep dp[i] as the largestDivisibleSubset size by position i, if nums[j] % nums[i] == 0, we don't need to check deep again.


nums.sort()
dp[0] = 1
dp[1] = 2 if nums[1] % nums[0] == 0 else 1
dp[i] = max(dp[k] + 1 if nums[i] % nums[k] == 0 else 1)

ans = max(dp)

'''

        if not nums or len(nums) == 1:
            return nums
        
        nums.sort()
        candidates = [[nums[0]]]
        
        for i in range(1, len(nums)):
            insert = False
            for j in range(len(candidates) - 1, -1, -1):
                if nums[i] % candidates[j][-1] == 0:
                    candidates.append(candidates[j] + [nums[i]])
                    insert = True
                    break
            
            if not insert:
                candidates.append([nums[i]])
            candidates.sort(key=lambda arr:len(arr))
        
        return sorted(candidates, key=lambda arr:len(arr))[-1]