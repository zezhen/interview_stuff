'''
https://leetcode.com/problems/combination-sum-iii

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:


	All numbers will be positive integers.
	The solution set must not contain duplicate combinations.


Example 1:


Input: k = 3, n = 7
Output: [[1,2,4]]


Example 2:


Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        candidates = range(1,10)
        self.combine([], candidates, 0, n, k)
        return [list(x) for x in set(tuple(x) for x in self.result)]
    
    def combine(self, cache, candidates, startIndex, target, k):
        _sum = sum(cache)
        for i in range(startIndex, len(candidates)):
            c = candidates[i]
            if _sum + c < target and len(cache) < k:
                cache.append(c)
                self.combine(cache, candidates, i+1, target, k)
                cache.pop()
            else:
                if _sum + c == target and len(cache) == k - 1:
                    self.result.append(cache[:] + [c])
                break