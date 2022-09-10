'''
https://leetcode.com/problems/subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:


Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
from collections import deque
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        def dfs(queue, start, n):
            ans.append(list(queue))
            
            for i in xrange(start, n):
                queue.append(nums[i])
                dfs(queue, i + 1, n)
                queue.pop()
        
        dfs(deque(), 0, len(nums))
        return ans

s = Solution()
print s.subsets([])
print s.subsets([1])
print s.subsets([1,2,3])