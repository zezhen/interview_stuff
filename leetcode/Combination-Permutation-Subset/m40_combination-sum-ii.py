'''
https://leetcode.com/problems/combination-sum-ii
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:


	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.


Example 1:


Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]


Example 2:


Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''
from collections import deque
class Solution(object):
    def combinationSum2(self, candidates, target):

        ans = []
        candidates.sort()

        def dfs(queue, acc_sum, target, start):
            if acc_sum == target:
                ans.append(list(queue))
                return

            for i in xrange(start, len(candidates)):
                if acc_sum + candidates[i] <= target:
                    queue.append(candidates[i])
                    dfs(queue, acc_sum + candidates[i], target, i+1)
                    queue.pop()
                else:
                    break

        dfs(deque(), 0, target, 0)
        return ans

    def combinationSum2_0(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        candidates.sort()
        self.combine([], candidates, 0, target)
        return [list(x) for x in set(tuple(x) for x in self.result)]
    
    def combine(self, cache, candidates, startIndex, target):
        _sum = sum(cache)
        for i in range(startIndex, len(candidates)):
            c = candidates[i]
            if _sum + c < target:
                cache.append(c)
                self.combine(cache, candidates, i+1, target)
                cache.pop()
            else:
                if _sum + c == target:
                    self.result.append(cache[:] + [c])
                break