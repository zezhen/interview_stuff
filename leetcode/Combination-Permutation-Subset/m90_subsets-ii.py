'''
https://leetcode.com/problems/subsets-ii
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:


Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''
from collections import deque
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        def dfs(queue, start, n):
            ans.append(list(queue))
            
            for i in xrange(start, n):
                if i > start and nums[i] == nums[i-1]: continue
                queue.append(nums[i])
                dfs(queue, i + 1, n)
                queue.pop()
        
        dfs(deque(), 0, len(nums))
        return ans

s = Solution()
print s.subsetsWithDup([1,2,2])