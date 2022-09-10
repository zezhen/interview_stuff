'''
https://leetcode.com/problems/combination-sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:


	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.


Example 1:


Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]


Example 2:


Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''
from collections import deque
class Solution(object):
    def combinationSum(self, candidates, target):

        ans = []
        candidates.sort()

        def dfs(queue, acc_sum, target, start):
            if acc_sum == target:
                ans.append(list(queue))
                return

            for i in xrange(start, len(candidates)):
                if acc_sum + candidates[i] <= target:
                    queue.append(candidates[i])
                    dfs(queue, acc_sum + candidates[i], target, i)
                    queue.pop()
                else:
                    break

        dfs(deque(), 0, target, 0)
        return ans

    def combinationSum0(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        candidates.sort()
        self.combine([], candidates, 0, target)
        return self.result
    
    def combine(self, cache, candidates, startIndex, target):
        _sum = sum(cache)
        for i in range(startIndex, len(candidates)):
            c = candidates[i]
            if _sum + c < target:
                cache.append(c)
                self.combine(cache, candidates, i, target)
                cache.pop()
            else:
                if _sum + c == target:
                    self.result.append(cache[:] + [c])
                break
            
            
            
        